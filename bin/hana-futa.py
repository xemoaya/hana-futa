import sys
import os
import math
import random
import json

MAX_PIORITY = 10

class card_obj :
    def __init__(self, env):
        self.name = env['name']
        self.pic = env['pic_name']
        self.type = env['type']
    def load_pic(self):
        pass#dummy function,load card picture

class rule_obj :
    def __init__(self, env) :
        self.rule = []
        for name in env :
            score = env[name]['score']
            for rul in env[name]['rule']:
                idx = rul.find('*')
                if idx == -1 :
                    self.rule.append({'name' : name, 'score' : score, 'base' : 0, 'showname':env[name]['showname'],\
                                    'card' : rul.split(','), 'priority' : env[name].get('priority', MAX_PIORITY) })
                else :
                    self.rule.append({'name' : name, 'score' : score, 'base' : int(rul[idx+1:]), 'showname':env[name]['showname'],\
                                    'card' : rul[:idx], 'priority' : env[name].get('priority', MAX_PIORITY) })
        self.rule.sort(key=lambda a:a['priority'])
    def test_rule(self):
#        for rul in self.rule :
            #print rul
        print self.judge_yaku(['sakura', 'phoenix'])
        print self.judge_yaku(['sakura', 'phoenix', 'tsuru'])
        print self.judge_yaku(['sakura', 'phoenix', 'tsuru', 'aoitan', 'tan', 'akatan', 'tan', 'aoitan', 'tan', 'aoitan', 'tan', 'tan', 'tan', \
        'moon', 'cup'])

    def judge_yaku(self, card_arr) :
        '''
        judge some player hit the yaku or not
        '''
        ret = {'yaku':{}, 'semi_yaku':{}}
        max_priority = MAX_PIORITY
        for rul in self.rule :
            if rul['base'] == 0 :#
                diff = set(rul['card']) - set(card_arr)
                print rul['card'],max_priority
                if not diff :#hit the rule
                    if rul['priority'] == MAX_PIORITY or rul['priority'] < max_priority :
                        max_priority = rul['priority'] 
                        if rul['name'] not in ret ['yaku'] :
                            ret ['yaku'][rul['name']] = rul['score']
                if len(diff) == 1 :
                    if rul['priority'] == MAX_PIORITY or rul['priority'] < max_priority :
                        if rul['name'] not in ret['yaku'] :
                            ret['semi_yaku'][rul['name']] = rul['score']
            else :
                cnt = card_arr.count(rul['card'])
                print cnt, rul['card']
                if cnt >= rul['base'] :
                    score = rul['score'] + cnt - rul['base']
                    if rul['name'] not in ret ['yaku'] or score > ret['yaku'][rul['name']]:
                        ret['yaku'][rul['name']] = score
                if cnt + 1 == rul['base'] :
                    if semi_yaku not in ret['yaku'] :
                        ret['semi_yaku'][rul['name']] = rul['score']

        return ret



class player :
    def __init__(self, role) :
        self.role = role#human or computer
        self.last_yaku = None
        self.mon = 0
        self.now_round = {}


global cards
global rules
def load_config(cfg_path) :
#load cards
    global cards
    cards = []
    data = json.load(file(cfg_path + 'card.json') )
    for mon in data :
        for card in mon['cards'] :
            cards.append(card_obj(card) )
#load rules
    global rules
    data = json.load(file(cfg_path + 'rule.json') )
    rules = rule_obj(data)
  
class game_table :
    def __init__(self) :
        self.yama_cards = []
        self.table_cards = []

if __name__ == '__main__' : 
    cfg_path = 'config/'#by default
    env = load_config(cfg_path)
    global rules
    rules.test_rule()
    #initial_table()
    #play_game()
