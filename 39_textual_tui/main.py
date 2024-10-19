from __future__ import annotations
import argparse

from typing import Any, ClassVar

from rich.syntax import Syntax
from textual import on
from textual.app import App, ComposeResult
from textual.binding import BindingType
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import DirectoryTree, Footer, Header, Static
from textual.reactive import reactive
from textual import events

class MyDirectoryTree(DirectoryTree):
    # Make show_root a reactive property
    show_root = reactive(True)

    def on_mount(self) -> None:
        # Initial setup or when mounted
        # self.path = "./"
        self.show_root = False  # Example: Set show_root to False

    def on_key(self, event: events.Key) -> None:
        # Example: Toggle show_root on key press
        if event.key == "t":
            self.show_root = not self.show_root

class DirectoryTreeApp(App):
    """
    The power of upath and fsspec in a Textual app
    """

    TITLE = "DirectoryTree"

    CSS = """
    DirectoryTree {
        max-width: 50%;
        width: auto;
        height: 100%;
        dock: left;
    }
    """

    BINDINGS: ClassVar[list[BindingType]] = [
        ("q", "quit", "Quit"),
    ]

    def __init__(self, path: str, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.path = path
        self.directory_tree = MyDirectoryTree(path=self.path)
        self.show_root = False
        self.file_content = Static(expand=True)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(self.directory_tree, VerticalScroll(self.file_content))
        yield Footer()

    # @on(DirectoryTree.FileSelected)
    # def handle_file_selected(self, message: DirectoryTree.FileSelected) -> None:
    #     """
    #     Do something with the selected file.

    #     Objects returned by the FileSelected event are upath.UPath objects and
    #     they are compatible with the familiar pathlib.Path API built into Python.
    #     """
    #     self.sub_title = str(message.path)
    #     try:
    #         file_content = message.path.read_text()
    #     except UnicodeDecodeError:
    #         self.file_content.update("")
    #         return None
    #     lexer = Syntax.guess_lexer(path=message.path.name, code=file_content)
    #     code = Syntax(code=file_content, lexer=lexer)
    #     self.file_content.update(code)

    @on(DirectoryTree.DirectorySelected)
    def handle_directory_selected(self, message: DirectoryTree.DirectorySelected) -> None:
        """
        Do something with the selected file.

        Objects returned by the FileSelected event are upath.UPath objects and
        they are compatible with the familiar pathlib.Path API built into Python.
        """
        self.sub_title = str(message.path)
        file_content = str(message)
        self.file_content.update(file_content)

    @on(DirectoryTree.NodeHighlighted)
    def handle_node_highlighted(self, event: DirectoryTree.NodeHighlighted) -> None:
        """Override the node selected behavior to prevent automatic expansion."""
        # Get the selected node
        node = event.node

        # Optionally, you could perform some action when the node is selected
        # For example, print the selected path
        self.file_content.update(f"Selected node: {node}")

        # Prevent expansion by not calling super().on_node_selected
        # The default behavior is expansion, so we avoid it by skipping this call.
        # Optionally, you could still expand it manually if needed.




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Skeleton")
    parser.add_argument("--path", dest="path", type=str, default="./", help="Path to the directory to display")
    args = parser.parse_args()

    app = DirectoryTreeApp(args.path)
    app.run()