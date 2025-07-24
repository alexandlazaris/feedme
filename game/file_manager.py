import matplotlib.pyplot
from player import PlayerClass
from enemy import EnemyClass
import json
from mplsoccer import Radar, grid
from matplotlib.font_manager import FontProperties
import matplotlib

default_font = FontProperties(family="DejaVu Sans", weight="regular")

def write_data(player: PlayerClass, enemy: EnemyClass):
    data_player = {
        "name": player.name,
        "maxHP": player.max_hp,
        "final_level": player.level,
        "total_xp": player.total_xp,
        "total_damage": player.total_dmg_taken,
        "hits_taken": player.total_number_of_hits,
        "start_time": player.start_time,
        "end_time": player.get_end_time(),
    }
    data_enemy = {
        "name": enemy.name,
        "maxHP": enemy.max_hp,
        "final_level": enemy.level,
        "total_xp": enemy.total_xp,
    }
    data = [data_player, data_enemy]
    data_string = json.dumps(data)
    file = open(f"./game/data.json", "w")
    file.write(data_string)
    file.close()


def generate_combined_graph(player: PlayerClass, enemy: EnemyClass, file_name: str):
    params = ["Maximum HP", "Level", "XP Gained", "Attack", "Defence"]
    player_values = [
        player.max_hp,
        player.level,
        player.total_xp,
        player.attack,
        player.defence,
    ]

    enemy_values = [enemy.hp, enemy.level, enemy.total_xp, enemy.attack, enemy.defence]

    radar = Radar(
        params,
        min_range=[0, 0, 0, 0, 0],
        max_range=[100, 100, 100, 100, 100],
        round_int=[True] * len(params),
        num_rings=5,
        ring_width=1,
        center_circle_radius=1,
    )

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

    radar.setup_axis(ax=axs["radar"])
    rings_inner = radar.draw_circles(
        ax=axs["radar"], facecolor="#ffb2b2", edgecolor="#fc5f5f"
    )
    radar_output = radar.draw_radar_compare(
        player_values,
        enemy_values,
        ax=axs["radar"],
        kwargs_radar={"facecolor": "#00f2c1", "alpha": 0.6},
        kwargs_compare={"facecolor": "#d80499", "alpha": 0.6},
    )
    radar_poly, radar_poly2, vertices1, vertices2 = radar_output
    range_labels = radar.draw_range_labels(
        ax=axs["radar"], fontsize=25, fontproperties=default_font
    )
    param_labels = radar.draw_param_labels(
        ax=axs["radar"], fontsize=25, fontproperties=default_font
    )
    axs["radar"].scatter(
        vertices1[:, 0],
        vertices1[:, 1],
        c="#00f2c1",
        edgecolors="#6d6c6d",
        marker="o",
        s=150,
        zorder=2,
    )
    axs["radar"].scatter(
        vertices2[:, 0],
        vertices2[:, 1],
        c="#d80499",
        edgecolors="#6d6c6d",
        marker="o",
        s=150,
        zorder=2,
    )

    endnote_text = axs["endnote"].text(
        0.99,
        0.5,
        "'Feed me': An RPG in your CLI.",
        fontsize=15,
        fontproperties=default_font,
        ha="right",
        va="center",
    )
    player_label_name = axs["title"].text(
        0.01,
        0.65,
        f"Player: {player.name}",
        fontsize=25,
        color="#01c49d",
        fontproperties=default_font,
        ha="left",
        va="center",
    )
    player_label_turns = axs["title"].text(
        0.01,
        0.25,
        f"Turns survived: {player.turns_taken}",
        fontsize=25,
        color="#01c49d",
        fontproperties=default_font,
        ha="left",
        va="center",
    )
    enemy_label_name = axs["title"].text(
        0.99,
        0.65,
        f"Enemy: {enemy.name}",
        fontsize=25,
        fontproperties=default_font,
        ha="right",
        va="center",
        color="#d80499",
    )
    enemy_label_phrase = axs["title"].text(
        0.99,
        0.25,
        f"Specialty: {enemy.specialty}",
        fontsize=25,
        fontproperties=default_font,
        ha="right",
        va="center",
        color="#d80499",
    )

    fig.savefig(file_name)
    matplotlib.pyplot.close()
