import re
from functools import lru_cache

from advent2022.utils.utils import Advent

advent = Advent(19)


def main():
    lines = advent.get_input_lines()
    blueprints = parse_blueprints(lines)
    total = 0
    for bp in blueprints:
        score = score_blueprint(bp)
        total += bp[0] * score
    print(1, total)


@lru_cache(maxsize=None)
def score_blueprint(
    costs: tuple[int, ...],
    resources: tuple[int, int, int] = (0, 0, 0),
    bots: tuple[int, int, int] = (1, 0, 0),
    t: int = 24,
) -> int:
    if t <= 1:
        return 0

    # Max number of bots we need for each resource going forward
    need_obs = bots[2] < costs[6]
    need_clay = bots[1] < costs[4]
    need_ore = bots[0] < max(costs[1], costs[2], costs[3], costs[5])

    # Which type of bot should we build ?
    build_geode = resources[0] >= costs[5] and resources[2] >= costs[6]
    build_obs = resources[0] >= costs[3] and resources[1] >= costs[4] and need_obs
    build_clay = resources[0] >= costs[2] and need_clay and need_obs
    build_ore = resources[0] >= costs[1] and need_ore

    score = 0
    if build_geode:
        # If we can build geode bot, this is the best option
        resources_ = (
            resources[0] + bots[0] - costs[5],
            resources[1] + bots[1],
            resources[2] + bots[2] - costs[6],
        )
        score = max(
            score,
            score_blueprint(costs, resources=resources_, bots=bots, t=t - 1) + t - 1,
        )
    elif build_obs:
        # If we can build obsidian bot, this is the second best option
        resources_ = (
            resources[0] + bots[0] - costs[3],
            resources[1] + bots[1] - costs[4],
            resources[2] + bots[2],
        )
        score = max(
            score,
            score_blueprint(
                costs,
                resources=resources_,
                bots=(bots[0], bots[1], bots[2] + 1),
                t=t - 1,
            ),
        )
    else:
        # Otherwise, consider building ore bot, clay bot, or simply mining
        if build_ore:
            resources_ = (
                resources[0] + bots[0] - costs[1],
                resources[1] + bots[1],
                resources[2] + bots[2],
            )
            score = max(
                score,
                score_blueprint(
                    costs,
                    resources=resources_,
                    bots=(bots[0] + 1, bots[1], bots[2]),
                    t=t - 1,
                ),
            )
        if build_clay:
            resources_ = (
                resources[0] + bots[0] - costs[2],
                resources[1] + bots[1],
                resources[2] + bots[2],
            )
            score = max(
                score,
                score_blueprint(
                    costs,
                    resources=resources_,
                    bots=(bots[0], bots[1] + 1, bots[2]),
                    t=t - 1,
                ),
            )
        resources_ = (
            resources[0] + bots[0],
            resources[1] + bots[1],
            resources[2] + bots[2],
        )
        score = max(
            score, score_blueprint(costs, resources=resources_, bots=bots, t=t - 1)
        )

    return score


def parse_blueprints(lines: list[str]) -> list[tuple[int, ...]]:
    blueprints = []
    for line in lines:
        m = re.match(
            r"Blueprint (\d+): Each ore robot costs (\d+) ore. "
            r"Each clay robot costs (\d)+ ore. "
            r"Each obsidian robot costs (\d+) ore and (\d+) clay. "
            r"Each geode robot costs (\d+) ore and (\d+) obsidian.",
            line,
        )
        if m is not None:
            blueprint = tuple(int(x) for x in m.groups())
            blueprints.append(blueprint)
    return blueprints


if __name__ == "__main__":
    main()
