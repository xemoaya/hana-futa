import sys
import os
import math
import random
import json

class card_obj :
    def __init__(self, env):
        self.name = env['id']
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
                    self.rule.append({'name' : name, 'score' : score, 'base' : 0, 'card' : rul.split(',')})
                else :
                    self.rule.append({'name' : name, 'score' : score, 'base' : int(rul[idx+1:]), 'card' : rul[:idx]})
    def test_rule(self):
        for rul in self.rule :
            print rul
    def judge_yaku(self, card_arr) :
        '''
        judge some player hit the yaku or not
        '''


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
