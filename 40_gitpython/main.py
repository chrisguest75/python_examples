import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import platform
from git import Repo


def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    """catches unhandled exceptions and logs them"""

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical(
        "Unhandled Exception {0}: {1}".format(exc_type, exc_value),
        extra={"exception": "".join(traceback.format_tb(exc_traceback))},
    )


def details() -> str:
    """return details about python version and platform as a dict"""
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "platform_details": platform.platform(),
    }


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def test(path: str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")
    logger.info(f"details={details()}")

    # search up for a .git directory
    if not os.path.exists(path):
        print(f"Path {path} does not exist")
        return 1
    
    if not os.path.isdir(path):
        print(f"Path {path} is not a directory")
        return 1
    
    if not os.path.exists(f"{path}/.git"):
        print(f"Path {path} is not a git repository")
        return 1

    print('-' * 40)
    print(f"path: {path}")
    print('-' * 40)
    repo = Repo(path)
    print(f"working_dir: {repo.working_dir}")
    default_branch = repo.git.symbolic_ref('refs/remotes/origin/HEAD').split('/')[-1]
    print(f"default_branch: {default_branch}")
    print(f"active_branch: {repo.active_branch}")
    head_commit = repo.git.rev_parse(default_branch)
    print(f"head_commit: {head_commit}")
    print(f"Dirty: {repo.is_dirty()}")
    print('-' * 40)
    print("Last 5 commits:")
    commits = list(repo.iter_commits(repo.active_branch, max_count=5))
    print('-' * 40)
    for commit in commits:
        print(f"Commit: {commit.hexsha}")
        print(f"Author: {commit.author.name} <{commit.author.email}>")
        print(f"Date: {commit.committed_datetime}")
        print(f"Message: {commit.message}")
        print('-' * 40)

    if repo.is_dirty():
        for item in repo.untracked_files:
            print(f"Untracked file: {item}")

    return 0


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="CLI Skeleton")
    parser.add_argument("--path", dest="path", type=str, default='./', help="path to the repo")
    args = parser.parse_args()

    success = test(args.path)

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
