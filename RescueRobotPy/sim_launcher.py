import os
import parser
import shutil
from tokenize import Double, String
from typing import List, Tuple, Dict
from enum import Enum
from math import sin, factorial, pow, exp

### Settings ###
# modify
mbt_module_dir = '/home/anna/Documenti/Uni/Tesi/mbt-module'
# do not modify
model = 'src/main/resources/rescuerobot.jmdp'
model_back = 'src/main/resources/rescuerobot.jmdp.back'
sim_out_file = 'mylogs.log'
gradle_build = './gradlew clean build'
gradle_run = './gradlew run -PappArgs="[\'-i\', \'' + model + '\']"'
################

class Action(Enum):
    INCREASE = 1
    DECREASE = 2

"""Preliminaries.

Semantic space
--------------
- battery: int in [1,100]
- quality: int in [1, 10]
- lights: float in [10.0, 10000.0]
- obstacleSize: float in [0.1, 2.0]

Definition of the rules (dictionary structure).
Each variable in the semantic space has one or more rules.
Each rule is a 5-tuple [arc, function, action, lowerbound, upperbound], where:
    arc : str
        specification of the arc target that shall match a line in the model (e.g., 'S0 e1 S1')
    function : str
        definition of a function that computes the offset to be applied to the target arc
    action : Action
        either add or subtract the computed offset to the base probability value
    lowerbound : float
        minimum offset value
    upperbound : float
        maximum offset value
"""

# battery
fb1 = "0.0001 * (100 - x)"
fb2 = "(" + fb1 + ") / 2"
# quality
fq1 = "((10-x) / ((10-x) + 1)) * 0.005"
fq2 = "(" + fq1 + ") / 2"
# lights
fl1 = "((x-10) / ((x-10) + 100)) * 0.025"
fl2 = "(" + fl1 + ") / 2"
# obstacleSize
fs1 = "0.001 * x * 4"
fs2 = "(" + fs1 + ") / 2"

rules = {
    'battery' : [
        ['S0 e1 S1', fb2, Action.INCREASE, 0.0, 0.01],
        ['S0 e1 S2', fb1, Action.DECREASE, 0.0, 0.01],
        ['S0 e1 S6', fb2, Action.INCREASE, 0.0, 0.01],
        ['S3 e1 S5', fb1, Action.INCREASE, 0.0, 0.01],
        ['S3 e1 S4', fb1, Action.DECREASE, 0.0, 0.01],
    ],
    'quality' : [
        ['S0 e1 S1', fq2, Action.INCREASE, 0.0, 0.005],
        ['S0 e1 S2', fq1, Action.DECREASE, 0.0, 0.005],
        ['S0 e1 S6', fq2, Action.INCREASE, 0.0, 0.005]
    ],
    'lights' : [
        ['S0 e1 S2', fl1, Action.INCREASE, 0.0, 0.025],
        ['S0 e1 S6', fl1, Action.DECREASE, 0.0, 0.025]
    ],
    'obstacleSize' : [
        ['S0 e1 S1', fs2, Action.DECREASE, 0.0, 0.005],
        ['S0 e1 S2', fs1, Action.INCREASE, 0.0, 0.005],
        ['S0 e1 S6', fs2, Action.DECREASE, 0.0, 0.005]
    ]
}

consistency_rules = {
    'S0 e1 S1' : 'S0 e1 S2',
    'S0 e1 S2' : 'S0 e1 S1',
    'S3 e1 S1' : 'S3 e1 S5',
    'S3 e1 S5' : 'S3 e1 S1',
    'S3 e1 S4' : 'S3 e1 S1',
    'S0 e1 S6' : 'S0 e1 S2'
}

def __force_inRange(value: float, lowerbound: float, upperbound: float) -> float:
    """Checks whether the given value is in [lowerbound, upperbound].
    If not, returns lowerbound in case value < lowerbound, upperbound otherwise.

    Parameters
    ----------
    value : float
    lowerbound : float
    upperbound : float
    """
    if value < lowerbound:
        return lowerbound
    if value > upperbound:
        return upperbound
    return value

def __apply_rule(line: str, rule: Tuple[str, str, Action, float, float], var_val: float) -> str:
    """Applies the rule in case of match.
    Returns the modified line if a match is not found.
    Returns None if a match is not found.

    Parameters
    ----------
    line : str
        line of the input model (e.g., "S0 e1 S2 0.80 u")
    rule : str
        rule to be applied (e.g., ['S0 e1 S1', f1, Action.INCREASE, 0.0, 0.02])
    """
    if line.startswith(rule[0]):
        base = float(line.split()[3])
        #if base > 0.0 and base < 1.0:
        fun = parser.expr(rule[1]).compile()
        x = var_val
        offset = __force_inRange(eval(fun), rule[3], rule[4])
        new_val = base
        if rule[2] == Action.INCREASE:
            new_val = new_val + offset
        elif rule[2] == Action.DECREASE:
            new_val = new_val - offset
        return rule[0] + ' ' + str(new_val) + ' u'
    return None

def gap(val1: float, val2: float) -> float:
    values = [val1, val2]
    values.sort()
    if values[0] < 0.0:
        if values[1] > 1.0 and abs(values[1] - 1.0) > abs(values[0]):
            return values[1] - 1.0
        else:
            return values[0]
        return values[0]
    else:
        if values[1] > 1.0:
            return values[1] - 1.0
    return 0.0

def __apply_singleVar(model_lines: List[str], rules: Dict[str, List[Tuple[str, str, Action, float, float]]], var_name: str, var_val: float, consistency_rules: Dict[str, str]) -> List[str]:
    """Applies all the changes to the model induced by the given var value.
    Return a list[str] representation of the model after applying all the changes.

    Parameters
    ----------
    model_lines : list[str]
        list of lines in the input model
    rules : dict
        dictionary that contains all the rules
    var_name : str
        variable of the semantic space (e.g., 'battery')
    var_val : float
        value assigned to the given variable (e.g., 'battery' -> 2.0)
    """
    exceptions = dict()
    result = list()
    i = 0
    for line in model_lines:
        target_rules = rules[var_name]
        for r in target_rules:
            new_line = __apply_rule(line, r, var_val)
            if new_line is not None:
                line_pieces = new_line.split()
                arc = line_pieces[0] + ' ' + line_pieces[1] + ' ' + line_pieces[2]
                prob = float(line_pieces[3])
                if prob < 0.0 or prob > 1.0:
                    exceptions.update({i : (arc, prob)})
                line = new_line
        result.append(line)
        i = i + 1
    #print('exceptions: {}'.format(exceptions))
    for i in exceptions:
        arc = exceptions[i][0]
        prob = exceptions[i][1]
        target_arc = consistency_rules[arc]
        k = [j for j in range(len(result)) if result[j].startswith(target_arc)][0]
        target_prob = float(result[k].split()[3])
        if k in exceptions:
            target_prob = exceptions[k][1]
        g = gap(prob, target_prob)
        if g > 0.0:
            if prob > target_prob:
                result[i] = arc + ' 1.0 u'
                exceptions.update({i : (arc, 1.0)})
                result[k] = target_arc + ' ' + str(target_prob + g) + ' u'
                if k in exceptions:
                    exceptions.update({k : (target_arc, target_prob + g)})
            else:
                result[i] = arc +  ' ' + str(prob + g) + ' u' ' 1.0 u'
                exceptions.update({i : (arc, prob + g)})
                result[k] = target_arc + ' 1.0 u'
                if k in exceptions:
                    exceptions.update({k : (target_arc, 1.0)})
        if g < 0.0:
            if prob < target_prob:
                result[i] = arc + ' 0.0 u'
                exceptions.update({i : (arc, 0.0)})
                result[k] = target_arc + ' ' + str(target_prob + g) + ' u'
                if k in exceptions:
                    exceptions.update({k : (target_arc, target_prob + g)})
            else:
                result[i] = arc +  ' ' + str(prob + g) + ' u'
                exceptions.update({i : (arc, prob + g)})
                result[k] = target_arc + ' 0.0 u'
                if k in exceptions:
                    exceptions.update({k : (target_arc, 0.0)})
        #print('result[{}]: {}'.format(i,result[i]))
        #print('result[{}]: {}'.format(k,result[k]))
        #print('exceptions: {}'.format(exceptions))
    return result

def apply_Vars(model_lines: List[str], rules: Dict[str, List[Tuple[str, str, Action, float, float]]], vars: List[Tuple[str, float]], consistency_rules: Dict[str, str]) -> List[str]:
    """Applies all the changes to the model induced by the given values assigned
    to the variables in the semantic space.
    Return a list[str] representation of the model after applying all the changes.

    Parameters
    ----------
    model_lines : list[str]
        list of lines in the input model
    rules : dict
        dictionary that contains all the rules
    vars : list[(str, float)]
        variables of the semantic space
        (e.g., [('battery', 2.0), ('lights', 1.5), ...)])
    """
    current_model = model_lines
    for v in vars:
        #print('__apply_singleVar call: {}'.format(v))
        current_model = __apply_singleVar(current_model, rules, v[0], v[1], consistency_rules)
    return current_model

def run_simulator(vars: List[Tuple[str, float]]) -> str:
    """Launches the simulator (mbt-module) after applying the changes induced by
    the variables in the semantic space.

    Parameters
    ----------
    vars : list[(str, float)]
        variables of the semantic space
        (e.g., [('battery', 2.0), ('lights', 1.5), ...)])
    """
    origin = os.getcwd()
    os.chdir(mbt_module_dir)

    shutil.copy2(model, model_back)

    initial_model = ''
    with open(model) as input_model:
        initial_model = input_model.read().splitlines()
    new_model = apply_Vars(initial_model, rules, vars, consistency_rules)
    #print(new_model)

    f = open(model, "w")
    f.write('\n'.join(new_model) + '\n')
    f.close()
    if os.path.exists(sim_out_file):
        os.remove(sim_out_file)

    os.system(gradle_build)
    log = os.popen(gradle_run).read()

    shutil.copy2(model_back, model)

    os.chdir(origin)

    return log

def get_regions(model_lines: List[str]) -> Dict[str, float]:
    regions_dict = { }
    for line in model_lines:
        if line.endswith(' u'):
            pieces = line.split()
            key = pieces[0] + ' ' + pieces[1] + ' ' + pieces[2]
            val = float(pieces[3])
            regions_dict[key] = val
    return regions_dict

def run_fast_try(vars: List[Tuple[str, float]]) -> Dict[str, float]:
    origin = os.getcwd()
    os.chdir(mbt_module_dir)

    initial_model = ''
    with open(model) as input_model:
        initial_model = input_model.read().splitlines()
    new_model = apply_Vars(initial_model, rules, vars, consistency_rules)

    regions = get_regions(new_model)

    os.chdir(origin)

    return regions

# example of invocation
