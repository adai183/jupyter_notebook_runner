import argparse
from datetime import datetime
import glob
import logging
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path
from simple_term_menu import TerminalMenu

logger = logging.getLogger(__name__)


def choose_nb(directory):
    """ show select menu on command line to pick notebook """
    nbs = glob.glob(f"{directory}/*.ipynb")
    terminal_menu = TerminalMenu(nbs)
    idx = terminal_menu.show()

    if idx != None:
        return Path(nbs[idx])


def run_notebook(input: Path, output: Path) -> None:
    """ run and save jupyter notebook """
    with open(input) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=None)
    ep.preprocess(nb, {"metadata": {"path": input.parent}})

    # create unique outpute path based on timestamp
    out_path = (
        output / f"run_{input.name}__{datetime.now().strftime('%Y%m%d%H%M%S%f')}.ipynb"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="notebooks",
        type=lambda p: Path(p).absolute(),
        required=False,
        help="Path to the notebook to be executed",
    )
    parser.add_argument(
        "--output",
        default="notebooks",
        type=lambda p: Path(p).absolute(),
        required=False,
        help="Path where to save the executed notebook containing all the output cells",
    )

    args = parser.parse_args()
    print(args)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO,
    )

    # make sure output directory exists
    args.output.parent.mkdir(parents=True, exist_ok=True)

    nb_path = choose_nb(args.input)

    logger.info(f"executing notebook {nb_path}")
    run_notebook(nb_path, args.output)
    logger.info("output saved to disk")


if __name__ == "__main__":
    main()
