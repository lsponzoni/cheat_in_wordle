def menu_item(menu_map, key):
    _f, description = menu_map[key]
    return key.upper() + ': ' + description

def menu_message(menu_map):
    menu_m = "Choose one:\n\t" 
    items = map((lambda k : menu_item(menu_map, k)), menu_map.keys()) 
    listing = "\n\t".join(items) 
    return menu_m + listing + '\n'

def read_prompt(ask):
    return input(ask).lower()

def prompt_for(ask, size):
    answer = ""
    while len(answer) != size:
        answer = read_prompt(ask)
    return answer

def run(menu, state, choice):
    function, _d = menu[choice]    
    return function(state)

def quit(state):
    return state, False

def stdMenu():
    return {'q': (quit, 'quit')}
