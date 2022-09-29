import argparse

### ! Put your imports here


### ! Define one or multiple functions, classes, etc. here.


def your_function(your_argument):

    ### ! Add a docstring to your function

    """_summary_

    Args:
        your_argument (_type_): _description_
    """

    pass


### ! Setup using __name__ == "__main__" allows the code defined above to be imported in other files, as well as the script to be run on its own.
if __name__ == "__main__":

    ### ! Argparser allows passing arguments to the script from the command line and provides an automatic help function with -h or --help.
    PARSER = argparse.ArgumentParser(
        description="""Description of what this script does."""
    )

    PARSER.add_argument(
        "-a",
        "--argument",
        default="argument",
        type=str,
        dest="a",
        help="Description of this argument.",
    )

    ### ! Add additional arguments here.

    ARGS = PARSER.parse_args()

    ### ! Call your function with the arguments passed from the argparser.
    your_function(your_argument=ARGS.a)
