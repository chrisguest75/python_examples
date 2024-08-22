from typing import List


class Trie:
    root = None

    class Node:
        # key = string, value = None || Node
        children = None
        end = False

        def __init__(self, components: List[str]):
            self.children = {}
            self.end = False
            self.add_child(components)

        def add_child(self, components: List[str]):
            if len(components) > 0:
                c = components[0]
                if len(components) == 1:
                    self.end = True

                if c in self.children:
                    self.children[c].add_child(components[1:])
                else:
                    self.children[c] = Trie.Node(components[1:])

        def find(self, components: List[str]):
            print(components, self.children, self.end)
            if len(components) > 0:
                c = components[0]
                if c in self.children:
                    if self.children[c] is None and len(components) == 0:
                        return True
                    else:
                        if len(components[1:]) > 0:
                            return self.children[c].find(components[1:])
                        else:
                            return self.end
                else:
                    return False
            else:
                return False

        def find_all(self, current, total):
            for k in self.children.keys():
                self.children[k].find_all(current + "/" + k, total)
            else:
                if self.end:
                    total.append(current + "/" + k)

            return total

    def __init__(self, paths):
        self.root = Trie.Node([])

        for p in paths:
            components = p.split("/")[1:]
            self.root.add_child(components)

    def contains(self, path: str):
        components = path.split("/")[1:]
        return self.root.find(components)

    def find_all(self):
        return self.root.find_all("", [])
