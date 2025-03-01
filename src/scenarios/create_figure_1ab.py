"""
This file contains the code for the creation of figure 1ab.
baseline model by country for with and
without trade scenarios.

Created on Wed Jul 15
@author: morgan
"""
import sys
from src.scenarios.run_model_no_trade import ScenarioRunnerNoTrade
from src.utilities.plotter import Plotter
import git
from pathlib import Path
import numpy as np

repo_root = git.Repo(".", search_parent_directories=True).working_dir


def call_scenario_runner(this_simulation, title):
    scenario_runner = ScenarioRunnerNoTrade()

    [world, pop_total, pop_fed, return_results] = scenario_runner.run_model_no_trade(
        title=title,
        create_pptx_with_all_countries=False,
        show_country_figures=False,
        show_map_figures=False,
        add_map_slide_to_pptx=False,
        scenario_option=this_simulation,
        countries_list=[],
    )

    return [world, pop_total, pop_fed]


def call_scenario_runner_with_and_without_fat_protein(this_simulation, title):
    this_simulation["scale"] = "country"
    this_simulation["crop_disruption"] = "country_nuclear_winter"
    this_simulation["grasses"] = "country_nuclear_winter"
    this_simulation["fish"] = "nuclear_winter"
    this_simulation["nutrition"] = "catastrophe"

    this_simulation["fat"] = "not_required"
    this_simulation["protein"] = "not_required"

    [world, pop_total, pop_fed] = call_scenario_runner(this_simulation, title)

    return world, round(100 * pop_fed / pop_total, 0)


def recalculate_plots():
    # WORST CASE #
    this_simulation = {}
    this_simulation["scenario"] = "no_resilient_foods"

    this_simulation["waste"] = "baseline_in_country"
    this_simulation["shutoff"] = "long_delayed_shutoff"
    this_simulation["meat_strategy"] = "inefficient_meat_strategy"

    this_simulation["buffer"] = "no_stored_between_years"
    this_simulation["seasonality"] = "no_seasonality"

    this_simulation["cull"] = "dont_eat_culled"
    worst_case_title = "No Adaptations"
    [
        world_worst_case,
        fraction_needs_worst_case,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation, worst_case_title
    )

    # WORST CASE + SIMPLE_ADAPTATIONS #

    this_simulation["waste"] = "tripled_prices_in_country"
    this_simulation["shutoff"] = "long_delayed_shutoff"
    this_simulation["meat_strategy"] = "efficient_meat_strategy"

    simple_adaptations_title = "simple_adaptations"
    [
        world_simple_adaptations,
        fraction_needs_simple_adaptations,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation, simple_adaptations_title
    )

    # WORST CASE + SIMPLE_ADAPTATIONS + CULLING #

    this_simulation["cull"] = "do_eat_culled"

    simple_adaptations_culling_title = "simple_adaptations,\nculling"
    [
        world_simple_adaptations_culling,
        fraction_needs_simple_adaptations_culling,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation, simple_adaptations_culling_title
    )

    # WORST CASE + SIMPLE_ADAPTATIONS + CULLING + STORAGE #
    this_simulation["buffer"] = "zero"
    this_simulation["seasonality"] = "country"
    example_scenario_title = (
        "Example Scenario:\nsimple_adaptations\n+ culling\n+ storage"
    )
    [
        world_example_scenario,
        fraction_needs_example_scenario,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation, example_scenario_title
    )

    this_simulation["scenario"] = "all_resilient_foods"
    all_resilient_foods_title = "Example Scenario\n + resilient foods"
    [
        world_example_scenario_resilient_foods,
        fraction_needs_example_scenario_resilient_foods,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation,
        all_resilient_foods_title,
    )

    # WORST CASE + SIMPLE_ADAPTATIONS + STORAGE + CULLING + ALL RESILIENT FOODS
    seaweed_title = "Example Scenario\n + seaweed"
    this_simulation["scenario"] = "seaweed"
    [
        world_seaweed,
        fraction_needs_seaweed,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation, seaweed_title
    )

    this_simulation["scenario"] = "methane_scp"
    methane_scp_title = "Example Scenario\n + methane_scp"
    [
        world_methane_scp,
        fraction_needs_methane_scp,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation, methane_scp_title
    )

    this_simulation["scenario"] = "cellulosic_sugar"
    cs_title = "Example Scenario\n+ cellulosic_sugar"
    [
        world_cellulosic_sugar,
        fraction_needs_cellulosic_sugar,
    ] = call_scenario_runner_with_and_without_fat_protein(this_simulation, cs_title)

    this_simulation["scenario"] = "relocated_crops"
    cold_crops_title = "Example Scenario\n+ cold_crops"
    [
        world_cold_crops,
        fraction_needs_cold_crops,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation, cold_crops_title
    )

    this_simulation["scenario"] = "greenhouse"
    greenhouse_title = "Example Scenario\n+ greenhouse_crops"
    [
        world_greenhouses,
        fraction_needs_greenhouses,
    ] = call_scenario_runner_with_and_without_fat_protein(
        this_simulation, greenhouse_title
    )

    worlds = {}
    worlds[worst_case_title] = world_worst_case
    worlds[simple_adaptations_title] = world_simple_adaptations
    worlds[simple_adaptations_culling_title] = world_simple_adaptations_culling
    worlds[example_scenario_title] = world_example_scenario
    worlds[all_resilient_foods_title] = world_example_scenario_resilient_foods
    worlds[seaweed_title] = world_seaweed
    worlds[methane_scp_title] = world_methane_scp
    worlds[cs_title] = world_cellulosic_sugar
    worlds[cold_crops_title] = world_cold_crops
    worlds[greenhouse_title] = world_greenhouses

    ratios = {}
    ratios[worst_case_title] = fraction_needs_worst_case
    ratios[simple_adaptations_title] = fraction_needs_simple_adaptations
    ratios[simple_adaptations_culling_title] = fraction_needs_simple_adaptations_culling
    ratios[example_scenario_title] = fraction_needs_example_scenario
    ratios[all_resilient_foods_title] = fraction_needs_example_scenario_resilient_foods
    ratios[seaweed_title] = fraction_needs_seaweed
    ratios[methane_scp_title] = fraction_needs_methane_scp
    ratios[cs_title] = fraction_needs_cellulosic_sugar
    ratios[cold_crops_title] = fraction_needs_cold_crops
    ratios[greenhouse_title] = fraction_needs_greenhouses

    return worlds, ratios


def main(args):
    RECALCULATE_PLOTS = True
    if RECALCULATE_PLOTS:
        the_path = Path(repo_root) / "results" / "large_reports" / "worlds1.npy"
        worlds, ratios = recalculate_plots()
        np.save(the_path, worlds)
        np.save(Path(repo_root) / "results" / "large_reports" / "ratios1.npy", ratios)
    else:
        worlds = np.load(
            Path(repo_root) / "results" / "large_reports" / "worlds1.npy",
            allow_pickle=True,
        ).item()
        ratios = np.load(
            Path(repo_root) / "results" / "large_reports" / "ratios1.npy",
            allow_pickle=True,
        ).item()

    Plotter.plot_fig_1ab_updated(worlds=worlds, ratios=ratios, xlim=72)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
