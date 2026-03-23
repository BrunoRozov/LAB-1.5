from models import Relationship
from browser import RelationshipBrowser


class Relationships(RelationshipBrowser):

    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for rel in self.relations:
            if rel[0].name == name and rel[1] == Relationship.PARENT:
                yield rel[2]

# Loeb kõik kokku.