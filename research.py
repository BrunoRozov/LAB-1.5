from browser import RelationshipBrowser


class Research:

    def __init__(self, browser: RelationshipBrowser):
        for child in browser.find_all_children_of("John"):
            print(f"John has a child called {child.name}") 

# Ütleb lause välja.