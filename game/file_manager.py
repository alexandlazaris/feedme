import matplotlib.pyplot
from player import PlayerClass
from enemy import EnemyClass
import json
from mplsoccer import Radar, grid
from matplotlib.font_manager import FontProperties
import matplotlib


def write_data(player: PlayerClass):
    data = {
        "player": player.name,
        "maxHP": player.max_hp,
        "final_level": player.level,
        "total_xp": player.total_xp,
        "total_damage": player.total_dmg_taken,
        "hits_taken": player.total_number_of_hits,
        "start_time": player.start_time,
        "end_time": player.get_end_time(),
    }
    data_string = json.dumps(data)
    file = open(f"./game/gameData.json", "w")
    file.write(data_string)
    file.close()


def generate_graph_type_one(player: PlayerClass):
    params = ["Maximum HP", "Level", "XP Gained", "Damage taken", "Hits taken"]
    values = [
        player.max_hp,
        player.level,
        player.total_xp,
        player.total_dmg_taken,
        player.total_number_of_hits,
    ]

    radar = Radar(
        params,
        # min_range=[0, 0, 0, 0, 0],
        min_range=[1, 1, 1, 1, 1],
        # max_range=[
        #     player.max_hp,
        #     player.level,
        #     player.total_xp,
        #     player.total_dmg_taken,
        #     player.total_number_of_hits,
        # ],
        max_range=[100, 100, 100, 100, 100],
        # max_range=[(player.max_hp+1)*10,
        #            (player.level+1)*10,
        #            (player.total_xp+1)*10,
        #            (player.total_dmg_taken+1)*10,
        #            (player.total_number_of_hits+1)*10],
        round_int=[True] * len(params),
        num_rings=2,
        ring_width=1,
        center_circle_radius=1,
    )
    default_font = FontProperties(family="DejaVu Sans", weight="regular")

    fig, ax = radar.setup_axis()
    rings_inner = radar.draw_circles(ax=ax, facecolor="#ffb2b2", edgecolor="#fc5f5f")
    radar_output = radar.draw_radar(
        values,
        ax=ax,
        kwargs_radar={"facecolor": "#6e9d00"},
        kwargs_rings={"facecolor": "#d4ff00"},
    )
    radar_poly, rings_outer, vertices = radar_output
    range_labels = radar.draw_range_labels(
        ax=ax, fontsize=15, fontproperties=default_font
    )
    param_labels = radar.draw_param_labels(
        ax=ax, fontsize=15, fontproperties=default_font
    )
    fig.savefig("radar_chart_1.png")


def generate_radar_graph_player(player: PlayerClass):
    params = ["Maximum HP", "Level", "XP Gained", "Damage taken", "Hits taken"]
    values = [
        player.max_hp,
        player.level,
        player.total_xp,
        player.total_dmg_taken,
        player.total_number_of_hits,
    ]

    radar = Radar(
        params,
        min_range=[0, 0, 0, 0, 0],
        # min_range=[1, 1, 1, 1, 1],
        max_range=[
            player.max_hp,
            player.level,
            player.total_xp,
            player.total_dmg_taken,
            player.total_number_of_hits,
        ],
        # max_range=[100, 100, 100, 100, 100],
        # max_range=[(player.max_hp+1)*1,
        #            (player.level+1)*1,
        #            (player.total_xp+1)*1,
        #            (player.total_dmg_taken+1)*1,
        #            (player.total_number_of_hits+1)*1],
        round_int=[True] * len(params),
        num_rings=2,
        ring_width=0.75,
        center_circle_radius=0.5,
    )

    default_font = FontProperties(family="DejaVu Sans", weight="regular")
    # creating the figure using the grid function from mplsoccer:
    fig, axs = grid(
        figheight=14,
        grid_height=0.915,
        title_height=0.06,
        endnote_height=0.025,
        title_space=0,
        endnote_space=0,
        grid_key="radar",
        axis=False,
    )

    # plot the radar
    radar.setup_axis(ax=axs["radar"])
    rings_inner = radar.draw_circles(
        ax=axs["radar"], facecolor="#ffb2b2", edgecolor="#fc5f5f"
    )
    radar_output = radar.draw_radar(
        values,
        ax=axs["radar"],
        kwargs_radar={"facecolor": "#5f9bfc", "alpha": 0.5},
        kwargs_rings={"facecolor": "#000000", "alpha": 0},
    )
    radar_poly, rings_outer, vertices = radar_output
    range_labels = radar.draw_range_labels(
        ax=axs["radar"], fontsize=25, fontproperties=default_font
    )
    param_labels = radar.draw_param_labels(
        ax=axs["radar"], fontsize=25, fontproperties=default_font
    )
    # adding the endnote and title text (these axes range from 0-1, i.e. 0, 0 is the bottom left)
    # Note we are slightly offsetting the text from the edges by 0.01 (1%, e.g. 0.99)
    title1_text = axs["title"].text(
        0.01,
        0.65,
        f"name: {player.name}",
        fontsize=25,
        fontproperties=default_font,
        ha="left",
        va="center",
    )
    title2_text = axs["title"].text(
        0.01,
        0.25,
        player.get_end_time(),
        fontsize=20,
        fontproperties=default_font,
        ha="left",
        va="center",
        color="#B6282F",
    )
    fig.savefig("radar_chart_player.png")
    matplotlib.pyplot.close()


def generate_radar_graph_enemy(enemy: EnemyClass):
    params = ["Maximum HP", "Level", "XP Gained", "Attack", "Defence"]
    values = [enemy.hp, enemy.level, enemy.total_xp, enemy.attack, enemy.defence]

    radar = Radar(
        params,
        min_range=[0, 0, 0, 0, 0],
        max_range=[enemy.hp, enemy.level, enemy.total_xp, enemy.attack, enemy.defence],
        # max_range=[100, 100, 100, 100, 100],
        # max_range=[
        #     (enemy.hp + 1) * 1,
        #     (enemy.level + 1) * 1,
        #     (enemy.total_xp + 1) * 1,
        #     (enemy.attack + 1) * 1,
        #     (enemy.defence + 1) * 1,
        # ],
        round_int=[True] * len(params),
        num_rings=2,
        ring_width=0.75,
        center_circle_radius=0.5,
    )

    default_font = FontProperties(family="DejaVu Sans", weight="regular")
    # creating the figure using the grid function from mplsoccer:
    fig, axs = grid(
        figheight=14,
        grid_height=0.915,
        title_height=0.06,
        endnote_height=0.025,
        title_space=0,
        endnote_space=0,
        grid_key="radar",
        axis=False,
    )

    # plot the radar
    radar.setup_axis(ax=axs["radar"])
    rings_inner = radar.draw_circles(
        ax=axs["radar"], facecolor="#ffb2b2", edgecolor="#fc5f5f"
    )
    radar_output = radar.draw_radar(
        values,
        ax=axs["radar"],
        kwargs_radar={"facecolor": "#5f9bfc", "alpha": 0.5},
        kwargs_rings={"facecolor": "#000000", "alpha": 0},
    )
    radar_poly, rings_outer, vertices = radar_output
    range_labels = radar.draw_range_labels(
        ax=axs["radar"], fontsize=25, fontproperties=default_font
    )
    param_labels = radar.draw_param_labels(
        ax=axs["radar"], fontsize=25, fontproperties=default_font
    )
    # adding the endnote and title text (these axes range from 0-1, i.e. 0, 0 is the bottom left)
    # Note we are slightly offsetting the text from the edges by 0.01 (1%, e.g. 0.99)
    title1_text = axs["title"].text(
        0.01,
        0.65,
        f"name: {enemy.name}",
        fontsize=25,
        fontproperties=default_font,
        ha="left",
        va="center",
    )
    fig.savefig("radar_chart_enemy.png")
    matplotlib.pyplot.close()
