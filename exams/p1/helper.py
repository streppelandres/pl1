import os
from player.PlayerAdapter import adapt_players
from player.Player import Player
from player.PlayerStats import PlayerStats
from utilities.files.json import json_utils
from utilities.files.csv import csv_utils


class Helper:
    '''
    A Helper class to hide spaghetti code and avoid mixed responsibilities
    '''
    __JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_data'))
    __CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_tmp'))
    __HALL_FAME_MEMBER_ARCHIVEMENT = 'Miembro del Salon de la Fama del Baloncesto'
    __ALL_STAR_ARCHIVEMENT = 'All-Star'

    players: list

    def __init__(self) -> None:
        '''
        Helper constructor, reads the json file with the data and adapt in classes
        '''
        self.players = adapt_players(json_utils.read_json(self.__JSON_PATH, 'dt')['jugadores'])
    
    def get_player_with_max_stat_attr(self, attr_name:str) -> Player:
        '''
        Gets the player with the max stat received
            attr_name: Stat attribute used to find the max
            returns: The player with the max attribute
        '''
        return max(self.players, key = lambda player : getattr(player.statistics, attr_name))
    
    def get_player_with_min_stat_attr(self, attr_name:str) -> Player:
        '''
        Gets the player with the min stat received
            attr_name: Stat attribute used to find the min
            returns: The player with the min attribute
        '''
        return min(self.players, key = lambda player : getattr(player.statistics, attr_name))

    @staticmethod
    def get_team_average_stat_by_attr(players:list, attr_name:str) -> float:
        '''
        Gets the average from the team by stat attr
            players: List of player to use the stats
            attr_name: Stat attribute used to calculate the average
            return: The average by attribute
        '''
        return sum(getattr(player.statistics, attr_name) for player in players) / len(players)
    
    def get_playeres_with_greater_stat_attr_than_value(self, attr_name:str, value:float) -> list:
        '''
        Get players list with stat attribute major to value passed by param
            attr_name: Attribute used to find greaters than value
            value: Value used to find greaters attrs
            return: Players list with major attr stat than value
        '''
        return list(filter(lambda player : getattr(player.statistics, attr_name) > value, self.players))
    
    def save_player_stats_to_csv(self, player:Player, file_name:str) -> bool:
        '''
            Save player stats to CSV
                player: Player to be saved
                file_name: CSV file name
        '''
        csv_head = ['name', 'position', 'seasons', 'total_points', 'average_points_per_game', 'total_rebounds',
                    'average_rebounds_per_game', 'total_assists', 'average_assists_per_game', 'total_steals',
                    'total_blocks', 'field_goal_percentage', 'free_throw_percentage', 'three_point_percentage']
        ps = player.statistics
        csv_body = [player.name, player.position, ps.seasons, ps.total_points, ps.average_points_per_game, ps.total_rebounds,
                    ps.average_rebounds_per_game, ps.total_assists, ps.average_assists_per_game, ps.total_steals, ps.total_blocks,
                    ps.field_goal_percentage, ps.free_throw_percentage, ps.three_point_percentage]
        csv_utils.save_csv(self.__CSV_PATH, file_name, [csv_head] + [csv_body])
    
    def get_player_archivements_by_name(self, player_name:str) -> list:
        '''
            Does what the function name says it does
                player_name: Player name to find
                returns: Player archivements
        '''
        return list(filter(lambda p : p.name.lower() == str(player_name).lower(), self.players))[0].archivements
    
    def is_hall_of_fame_player_by_name(self, player_name:str) -> bool:
        '''
            Does what the function name says it does
                player_name: Player name to find
                returns: True if the player is part of the fame hall, False otherwise
        '''
        return Helper.__HALL_FAME_MEMBER_ARCHIVEMENT in self.get_player_archivements_by_name(player_name)
    
    def get_player_with_more_archivements(self) -> Player:
        '''
            Does what the function name says it does
                returns: Player with more archivements
        '''
        return max(self.players, key = lambda player : len(player.archivements))

    def __sort_players_by_stat_attr(self, attr_name:str, reverse:bool=False) -> list:
        '''
            Sort players by the stat attribute passed by param
                attr_name: Stat attribute used to sort
                reverse: For ascending/descending sorting, default is False
                returns: List of players sorted
        '''
        return sorted(self.players, key = lambda player : getattr(player.statistics, attr_name), reverse=reverse)

    def get_ranking(self) -> dict:
        '''
            Creates a dictionary with the player position in these stats:
            'total_points', 'total_rebounds', 'total_assists', 'total_steals'
            Using the players name by key
                returns: Dictionary with player name key, and the ranking position in the stats
        '''
        ranking = {}
        for attr in ['total_points', 'total_rebounds', 'total_assists', 'total_steals']:
            for i, p in enumerate(self.__sort_players_by_stat_attr(attr, True)):
                # Si no existe la key del jugador, lo crea
                if not p.name in ranking.keys():
                    ranking[p.name] = {}
                # Si no existe la key del attr en la key del jugador, lo crea
                if not attr in ranking[p.name].keys():
                    ranking[p.name][attr] = 0
                # El index sería la posición en el ranking del jugador con ese attr
                ranking[p.name][attr] = i + 1
        return ranking

    def save_ranking_to_csv(self, ranking:dict, file_name:str) -> None:
        '''
            Save ranking to CSV
        '''
        csv_head = ['player', 'points', 'rebounds', 'assist', 'steals']
        csv_body = [[p] + list(ranking[p].values()) for p in ranking]
        csv_utils.save_csv(self.__CSV_PATH, file_name, [csv_head] + csv_body)

    def __get_grouped_players_by_key(self, key): 
        grouped_players = {}
        
        # FIXME: Código medio repetido con get_ranking
        for player in self.players:
            if getattr(player, key) in grouped_players.keys():
                grouped_players[getattr(player, key)].append(player)
            else:
                grouped_players[getattr(player, key)] = []
                grouped_players[getattr(player, key)].append(player)

        return grouped_players

    def get_grouped_quantity_of_players_by_key(self, key):
        grouped_players = self.__get_grouped_players_by_key(key)
        return {k: len(grouped_players[k]) for k in grouped_players}

    def get_all_star_players(self):
        all_star_players = []

        # TODO: Hacelo en modo Python
        for player in self.players:
            for archivement in player.archivements:
                # FIXME: Esto con expresiones regulares estaría mejor
                if self.__ALL_STAR_ARCHIVEMENT in archivement:
                    all_star_players.append({
                        "name": player.name,
                        "quantity": int(archivement.split(' ')[0])
                    })
                    break
        
        return sorted(all_star_players, key=lambda p : p['quantity'], reverse=True)
    
    def get_best_stats_players(self):

        def __build_best_by_stat(stat_attr):
            player = self.get_player_with_max_stat_attr(stat_attr)
            return {
                "name": player.name,
                "stat": getattr(player.statistics, stat_attr),
                "text": stat_attr.replace("_", " ").capitalize()
            }
        
        return [
            __build_best_by_stat('seasons'),
            __build_best_by_stat('total_points'),
            __build_best_by_stat('average_points_per_game'),
            __build_best_by_stat('total_rebounds'),
            __build_best_by_stat('average_rebounds_per_game'),
            __build_best_by_stat('total_assists'),
            __build_best_by_stat('average_assists_per_game'),
            __build_best_by_stat('total_steals'),
            __build_best_by_stat('total_blocks'),
            __build_best_by_stat('field_goal_percentage'),
            __build_best_by_stat('free_throw_percentage'),
            __build_best_by_stat('three_point_percentage'),
        ]
    

    def get_best_player(self) -> Player:
        return max(self.players, key=lambda p : sum(vars(p.statistics).values()))