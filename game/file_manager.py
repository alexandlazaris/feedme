from player import PlayerClass
import json
from mplsoccer import Radar, FontManager, grid
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt


def write_data(player: PlayerClass):
    print("writing data to file")
    data = {
        "player": player.name,
        "maxHP": player.maxHP,
        "final_level": player.totalLvlUps,
        "total_xp": player.getTotalExp(),
        "total_damage": player.getTotalDamageTaken(),
        "hits_taken": player.getNumberOfHits(),
        "start_time": player.getStartTime(),
        "end_time": player.getEndTime(),
    }
    data_string = json.dumps(data)
    file = open(f"./game/gameData.json", "w")  # file.truncate(0)
    file.write(data_string)
    file.close()


def generate_graph(player: PlayerClass):
    # df = pd.DataFrame(dict(
    # r=[player.maxHP, player.totalLvlUps, player.getTotalExp(), player.getTotalDamageTaken(), player.getNumberOfHits()],
    # theta=['maxHP','final_level','total_xp',
    #        'total_damage', 'hits_taken']))
    # fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    # fig.show()

    # Data
    params = ["maxHP", "final_level", "total_xp", "total_damage", "hits_taken"]
    values = [
        player.maxHP,
        player.totalLvlUps,
        player.getTotalExp(),
        player.getTotalDamageTaken(),
        player.getNumberOfHits(),
    ]

    radar = Radar(
        params,
        min_range=[0, 0, 0, 0, 0],
        max_range=[100, 100, 100, 100, 100],
        # whether to round any of the labels to integers instead of decimal places
        round_int=[False] * len(params),
        num_rings=4,  # the number of concentric circles (excluding center circle)
        # if the ring_width is more than the center_circle_radius then
        # the center circle radius will be wider than the width of the concentric circles
        ring_width=1,
        center_circle_radius=1,
    )


    default_font = FontProperties(family='DejaVu Sans', weight='regular')


    fig, ax = radar.setup_axis()  # format axis as a radar
    rings_inner = radar.draw_circles(
        ax=ax, facecolor="#ffb2b2", edgecolor="#fc5f5f"
    )  # draw circles
    radar_output = radar.draw_radar(
        values,
        ax=ax,
        kwargs_radar={"facecolor": "#aa65b2"},
        kwargs_rings={"facecolor": "#66d8ba"},
    )  # draw the radar
    radar_poly, rings_outer, vertices = radar_output
    range_labels = radar.draw_range_labels(
        ax=ax, fontsize=15, fontproperties=default_font
    )  # draw the range labels
    param_labels = radar.draw_param_labels(
        ax=ax, fontsize=15, fontproperties=default_font
    )  # draw the param labels
    fig.savefig("radar_chart.png")
