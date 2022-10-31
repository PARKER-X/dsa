class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self 
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level


    def print_tree(self):
        spaces = " "*self.get_level() *3
        prefix = spaces + "|____" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_trees():
    root = TreeNode('Electronics')
    
    tv = TreeNode('Tv')
    tv.add_child(TreeNode('Apple Tv'))
    tv.add_child(TreeNode('Ak'))
    game = TreeNode('Game')
    game.add_child(TreeNode('KO'))
    game.add_child(TreeNode('Xtream'))


    root.add_child(tv)
    root.add_child(game)
    root.print_tree()

    

if __name__=="__main__":
    build_trees()
    

        