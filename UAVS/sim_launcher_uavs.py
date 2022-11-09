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
#mbt_module_dir = '/Users/matteocamilli/tools/mbt-module'
# do not modify
model = 'src/main/resources/uavs.jmdp'
model_back = 'src/main/resources/uavs.jmdp.back'
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
- formation: int in [0,1] (tight, loose)
- flying speed: float in [5, 50] mph
- countermeasure: int in [0, 1] No/Yes
- weather: int in [1, 2, 3, 4] (sun, clouds, rain, fog)
- day time: int in [0, 24]
- threat range: float in [1.0, 4.0] km
- #threats: int in [1, 10]
    

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

# formation (increase prob detection at low levels)
f_form_r1_1 = "0.001 * x"
f_form_r1_2 = "(" + f_form_r1_1 + ") / 2"
f_form_r2_1 = "0.0015 * x"
f_form_r2_2 = "(" + f_form_r2_1 + ") / 2"
# flying speed (decreases prob detection)
f_speed_1 = "((x-5) / ((x-5) + 100)) * 0.005"
f_speed_2 = "(" + f_speed_1 + ") / 2"
f_speed_3 = "(" + f_speed_1 + ") / 3"
# countermeasure (decreases prob detection)
f_counter_1 = "0.005 * x"
f_counter_2 = "(" + f_counter_1 + ") / 2"
# weather (decreases prob detection at high levels)
f_weather_1 = "0.0005 * x"
f_weather_2 = "(" + f_weather_1 + ") / 2"
# day time (no effect)
# -
# threat range (decreases prob detection)
f_threat_1 = "((x-1.0) / ((x-1.0) + 0.1)) * 0.002"
f_threat_2 = "(" + f_threat_1 + ") / 2"
f_threat_3 = "(" + f_threat_1 + ") / 3"
# threats (increases prob detection)
f_nthreats_1 = "0.0045 - (((10-x) / ((10-x) + 1)) * 0.005)"
f_nthreats_2 = "(" + f_nthreats_1 + ") / 2"
f_nthreats_3 = "(" + f_nthreats_1 + ") / 3"

rules = {
    'formation' : [
        ['S0 sTrt S21', f_form_r1_1, Action.INCREASE, 0.0, 0.001],
        ['S0 sTrt S1', f_form_r1_1, Action.DECREASE, 0.0, 0.001],
        ['S7 sTrt S21', f_form_r2_1, Action.INCREASE, 0.0, 0.0015],
        ['S7 sTrt S6', f_form_r2_2, Action.DECREASE, 0.0, 0.00075],
        ['S7 sTrt S8', f_form_r2_2, Action.DECREASE, 0.0, 0.00075]
    ],
    'flying_speed' : [
        ['S0 sTrt S21', f_speed_1, Action.DECREASE, 0.0, 0.0016],
        ['S0 sTrt S1', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S0 sTrt S22', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S7 sTrt S21', f_speed_1, Action.DECREASE, 0.0, 0.0016],
        ['S7 sTrt S6', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S7 sTrt S8', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S7 sTrt S22', f_speed_1, Action.DECREASE, 0.0, 0.0016],
        ['S7 sTrt S6', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S7 sTrt S8', f_speed_2, Action.INCREASE, 0.0, 0.0008],    
        ['S14 sTrt S21', f_speed_1, Action.DECREASE, 0.0, 0.0016],
        ['S14 sTrt S13', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S14 sTrt S15', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S14 sTrt S22', f_speed_1, Action.DECREASE, 0.0, 0.0016],
        ['S14 sTrt S13', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S14 sTrt S15', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S20 sTrt S21', f_speed_1, Action.DECREASE, 0.0, 0.0016],
        ['S20 sTrt S19', f_speed_2, Action.INCREASE, 0.0, 0.0008],
        ['S20 sTrt S22', f_speed_2, Action.INCREASE, 0.0, 0.0008]
    ],
    'countermeasure' : [
        ['S0 sTrt S21', f_counter_1, Action.DECREASE, 0.0, 0.005],
        ['S0 sTrt S1', f_counter_1, Action.INCREASE, 0.0, 0.005],
        ['S7 sTrt S21', f_counter_1, Action.DECREASE, 0.0, 0.005],
        ['S7 sTrt S6', f_counter_2, Action.INCREASE, 0.0, 0.0025],
        ['S7 sTrt S8', f_counter_2, Action.INCREASE, 0.0, 0.0025],
        ['S14 sTrt S21', f_counter_1, Action.DECREASE, 0.0, 0.005],
        ['S14 sTrt S6', f_counter_2, Action.INCREASE, 0.0, 0.0025],
        ['S14 sTrt S8', f_counter_2, Action.INCREASE, 0.0, 0.0025],
        ['S20 sTrt S21', f_counter_1, Action.DECREASE, 0.0, 0.005],
        ['S20 sTrt S19', f_counter_1, Action.INCREASE, 0.0, 0.005]
    ],
    'weather' : [
       ['S14 sTrt S21', f_weather_1, Action.DECREASE, 0.0, 0.002],
       ['S14 sTrt S6', f_weather_2, Action.INCREASE, 0.0, 0.001],
       ['S14 sTrt S8', f_weather_2, Action.INCREASE, 0.0, 0.001],
       ['S20 sTrt S21', f_weather_1, Action.DECREASE, 0.0, 0.002],
       ['S20 sTrt S19', f_weather_1, Action.INCREASE, 0.0, 0.002]
    ],
    'day_time' : [
        
    ],
    'threat_range' : [
        ['S0 sTrt S21', f_threat_1, Action.INCREASE, 0.0, 0.002],
        ['S0 sTrt S1', f_threat_1, Action.DECREASE, 0.0, 0.002],
        ['S7 sTrt S21', f_threat_1, Action.INCREASE, 0.0, 0.002],
        ['S7 sTrt S6', f_threat_2, Action.DECREASE, 0.0, 0.001],
        ['S7 sTrt S8', f_threat_2, Action.DECREASE, 0.0, 0.001], 
        ['S14 sTrt S21', f_threat_1, Action.INCREASE, 0.0, 0.002],
        ['S14 sTrt S6', f_threat_2, Action.DECREASE, 0.0, 0.001],
        ['S14 sTrt S8', f_threat_2, Action.DECREASE, 0.0, 0.001],       
        ['S20 sTrt S21', f_threat_1, Action.INCREASE, 0.0, 0.002],
        ['S20 sTrt S19', f_threat_1, Action.DECREASE, 0.0, 0.002]
    ],
    'threats' : [
        ['S0 sTrt S21', f_nthreats_1, Action.INCREASE, 0.0, 0.0025],
        ['S0 sTrt S1', f_nthreats_1, Action.DECREASE, 0.0, 0.0025],
        ['S7 sTrt S21', f_nthreats_1, Action.INCREASE, 0.0, 0.0025],
        ['S7 sTrt S6', f_nthreats_2, Action.DECREASE, 0.0, 0.00125],
        ['S7 sTrt S8', f_nthreats_2, Action.DECREASE, 0.0, 0.00125], 
        ['S14 sTrt S21', f_nthreats_1, Action.INCREASE, 0.0, 0.0025],
        ['S14 sTrt S6', f_nthreats_2, Action.DECREASE, 0.0, 0.00125],
        ['S14 sTrt S8', f_nthreats_2, Action.DECREASE, 0.0, 0.00125],       
        ['S20 sTrt S21', f_nthreats_1, Action.INCREASE, 0.0, 0.0025],
        ['S20 sTrt S19', f_nthreats_1, Action.DECREASE, 0.0, 0.0025]
    ]
}

consistency_rules = {
    'S0 sTrt S21' : 'S0 sTrt S1',
    'S0 sTrt S1' : 'S0 sTrt S21',
    'S0 sTrt S22' : 'S0 sTrt S1',
    'S7 sTrt S21' : 'S7 sTrt S6',
    'S7 sTrt S6' : 'S7 sTrt S8',
    'S7 sTrt S22' : 'S7 sTrt S6',
    'S14 sTrt S21' : 'S14 sTrt S13',
    'S14 sTrt S22' : 'S14 sTrt S13',
    'S14 sTrt S13' : 'S7 sTrt S15',
    'S20 sTrt S21' : 'S20 sTrt S22',
    'S20 sTrt S22' : 'S20 sTrt S19',
    'S20 sTrt S19' : 'S20 sTrt S22'
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
