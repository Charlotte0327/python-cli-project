import typer
from rich import print
from typing import Annotated

app = typer.Typer()

@app.command()

def greeting(
    name: Annotated[str, typer.Argument(help = "This is Optional")] = None, # Optional
    lastname: str = typer.Argument(help = "This is Required --> "), # Required (Normally required before optional)
    informal: bool = False
    ):    # How these work by default 


    if informal:   # Use --informal and prints infrmail greeting 
        print(f"Hello {name} {lastname}!")
    else:
        print(f"Good day Ms. {name} {lastname}.")



if __name__ == "__main__":
    app()
     