import copy
from utilities.console.console_utils import clear_console, request_input, request_int_in_range, request_string, request_int
from config.parser import load_config
from helper import Helper

JSON_DATA_PATH = './data/heroes.json'
INI_CONFIG_PATH = './config/menu.ini'

class App:
    '''
    A App class to hide spaghetti code and (try) avoid mixed responsibilities
    '''
    helper: Helper
    menu: str
    menu_splited: list
    options: dict

    def __init__(self) -> None:
        '''
        App constructor, initialize helper, read menu options from config file and map the menu options
        '''
        self.helper = Helper()
        self.menu = load_config(INI_CONFIG_PATH)['MENU']['es']
        self.menu_splited = self.menu.splitlines()
        self.options = {
            '1': self.option_1, '2': self.option_2,
            '3': self.option_3, '4': self.option_4,
            '5': self.option_5, '6': self.option_6,
            '7': self.option_7, '8': self.option_8,
            '9': self.option_9, '10': self.option_10,
            '11': self.option_11, '12': self.option_12,
            '13': self.option_13, '14': self.option_14,
            '15': self.option_15, '16': self.option_16,
            '17': self.option_17, '18': self.option_18,
            '19': self.option_19, '20': self.option_20,
            '21': self.option_21, '22': self.option_22,
            '23': self.option_23, '24': self.option_24,
            'X': self.option_exit
        }

    def start(self):
        '''
        Start function, with the inifinite loop wait for users inpu, shows the menu, and validate selected option
        '''
        while True:
            clear_console()
            option = input(self.menu + '\n').upper()
            clear_console()
            if option in self.options:
                self.__print_menu_option(option)
                self.options[option]()
            else:
                print('Opción incorrecta, vuelva a intentar\n')
            request_input()

    def __print_menu_option(self, option_index:str):
        '''
        Prints the selected menu option passed by param
            option_index: User selected option
        '''
        print(self.menu_splited[option_index.isnumeric() and int(option_index) or len(self.menu_splited) - 1] + '\n')

    def __request_player_by_name(self) -> str:
        '''
        Request a player name to the user, and validates if exist
            returns The valid player name
        '''
        print(''.join([f'{player.name}\n' for player in self.helper.players]))
        return request_string('Ingrese el nombre del jugador a buscar:\n', [p.name for p in self.helper.players], 'Por favor, ingrese un nombre valido:\n')

    def __print_playeres_with_greater_stat_attr_than_value(self, message:str, attr_name:str, sort_attr:str=None) -> None:
        '''
            Semi-generic function who request a number to after find and print players with greater stat attribute than passed by param
                message: Message to display in console
                attr_name: Stat attribute name
                sort_attr: Attribute used to sort the results
        '''
        greater_than = request_int(f'{message}\n', 'Por favor, ingrese un número válido')
        players = self.helper.get_playeres_with_greater_stat_attr_than_value(attr_name, greater_than)
        if players:
            print(f'Jugadores con {attr_name.replace("_", " ")} mayor a {greater_than}:\n')
            print('\n'.join([f'{player.name}{sort_attr == None and " " or " [" + getattr(player, sort_attr) + "]"}- {getattr(player.statistics, attr_name)}' for player in (sort_attr == None and players or sorted(players, key = lambda p : getattr(p, sort_attr)))]))
        else:
            print(f'No se encontraron jugadores con {attr_name.replace("_", " ")} mayor a {greater_than}\n')
    
    def __print_player_with_max_stat_attr(self, attr_name:str) -> None:
        '''
            Prints player with the max attr passed by param
                attr_name: Stat attribute to find the max
        '''
        player = self.helper.get_player_with_max_stat_attr(attr_name)
        print(f'{player.name} - {getattr(player.statistics, attr_name)}\n')

    def option_1(self):
        print(''.join([f'{player.name} - {player.position}\n' for player in self.helper.players]))

    def option_2(self):
        players = [f'{i} - {player.name} - {player.position}\n' for i, player in enumerate(self.helper.players)]
        print(''.join(players))
        player = self.helper.players[request_int_in_range('Ingrese un indice para poder ver sus estadísticas:\n', 0, len(players))]
        clear_console()
        print(player.name)
        print(player.statistics)
        self.helper.save_player_stats_to_csv(player, f'player_stats_{player.name.lower().replace(" ", "_")}')

    def option_3(self):
        print('\n'.join(self.helper.get_player_archivements_by_name(self.__request_player_by_name())))

    def option_4(self):
        print(f'Promedio del equipo: {format(Helper.get_team_average_stat_by_attr(self.helper.players, "average_points_per_game"), ".2f")}')
        print(''.join([f'{player.name} - {player.statistics.average_points_per_game}\n' for player in sorted(self.helper.players, key = lambda p : p.name)]))

    def option_5(self):
        player_name = self.__request_player_by_name()
        print(f'{player_name.capitalize()} {self.helper.is_hall_of_fame_player_by_name(player_name) and "es" or "no es"} miembro del salón de la fama')

    def option_6(self):
        self.__print_player_with_max_stat_attr('total_rebounds')

    def option_7(self):
        self.__print_player_with_max_stat_attr('field_goal_percentage')

    def option_8(self):
        self.__print_player_with_max_stat_attr('total_assists')

    def option_9(self):
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un promedio de puntos por partido:', 'average_points_per_game')

    def option_10(self):
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un promedio de rebotes por partido:', 'average_rebounds_per_game')

    def option_11(self):
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un promedio de asistencias por partido:', 'average_assists_per_game')
    
    def option_12(self):
        self.__print_player_with_max_stat_attr('total_steals')

    def option_13(self):
        self.__print_player_with_max_stat_attr('total_blocks')
    
    def option_14(self):
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un porcentaje de tiros libres por partido:', 'free_throw_percentage')
    
    def option_15(self):
        player = self.helper.get_player_with_min_stat_attr('average_points_per_game')
        players_copy = copy.deepcopy(self.helper.players)
        players_copy.remove(player)
        average = Helper.get_team_average_stat_by_attr(players_copy, 'average_points_per_game')
        print(f'Jugador con promedio más bajo: {player.name} - {player.statistics.average_points_per_game}')
        print(f'Promedio del equipo sin el jugador con el promedio más bajo: {format(average, ".2f")}')
    
    def option_16(self):
        player = self.helper.get_player_with_more_archivements()
        print(f'Jugador con más logros: {player.name}, cantidad: {len(player.archivements)}')
        print(f'Logros:')
        print('\n'.join(player.archivements))
    
    def option_17(self):
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un porcentaje de triples:', 'three_point_percentage')

    def option_18(self):
        self.__print_player_with_max_stat_attr('seasons')
    
    def option_19(self):
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un porcentaje de tiros de campo:', 'field_goal_percentage', sort_attr='position')
    
    def option_20(self):
        ranking = self.helper.get_ranking()

        for p in ranking:
            v = [str(v) for v in ranking[p].values()]
            print(f'{p}, puntos: {v[0]}, rebotes: {v[1]}, asistencias: {v[2]}, robos: {v[3]}')
        
        self.helper.save_ranking_to_csv(ranking, '23_bonus_ranking')
    
    def option_21(self):
        grouped_by_position = self.helper.get_grouped_quantity_of_players_by_key('position')
        r = '\n'.join([f'{p}: {grouped_by_position[p]}' for p in grouped_by_position])
        print(r)
    
    def option_22(self):
        all_star_players = self.helper.get_all_star_players()
        r = [f'{dict(p)["name"]} ({dict(p)["quantity"]} veces All-Star)' for p in all_star_players]
        print('\n'.join(r))
    
    def option_23(self):
        r = []
        for best in self.helper.get_best_stats_players():
            best = dict(best)
            r.append(
                f'Mayor cantidad de {best["text"]}: {best["name"]} ({best["stat"]})'
            )
        print('\n'.join(r))

    def option_24(self):
        best_player = self.helper.get_best_player()
        print(f'El jugador con el mayor de todas sus estadisticas sumadas es: {best_player.name}')

    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)
