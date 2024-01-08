class Symbol:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.value = ""


class SymbolTable:
    def __init__(self):
        self.symbols = [Symbol() for _ in range(MAX_SYMBOLS)]


class Node:
    def __init__(self):
        self.scopeSymbolTable = SymbolTable()  # Table of symbols for the current scope
        self.symbolCount = 0  # Count of symbols in the current scope
        self.nextSibling = None  # Reference to the next node in the scope chain

    def push_scope(self):
        """
        Creates a new scope node and sets it as the current scope.
        Returns:
            Node: The new scope node.
        """
        newScopeNode = Node()
        newScopeNode.nextSibling = self
        return newScopeNode

    def pop_scope(self):
        """
        Removes the current scope and returns to the previous scope.
        Returns:
            Node: The previous scope node or None if no more scopes.
        """
        if self is not None:
            self = self.nextSibling
            return self
        else:
            print("Cannot pop from an empty symbol table")
            return self

    def print_current_scope(self):
        if self is not None:
            print("Current Scope Symbols:")
            for i in range(self.symbolCount):
                symbol = self.scopeSymbolTable.symbols[i]
                if isinstance(symbol.value, float):
                    print(f"{symbol.name}\t {symbol.value:.6f}")
                else:
                    print(f"{symbol.name}\t {symbol.value}")
            print("\n")
        else:
            print("Symbol table is empty")


    def print_all_scopes(self):
        currentNode = self
        while currentNode is not None:
            print("Scope Symbols:")
            for i in range(currentNode.symbolCount):
                symbol = currentNode.scopeSymbolTable.symbols[i]
                if isinstance(symbol.value, float):
                    print(f"{symbol.name}\t {symbol.value:.6f}")
                else:
                    print(f"{symbol.name}\t {symbol.value}")
            print("\n")
            currentNode = currentNode.nextSibling


    def insert_symbol(self, symbol_type, symbol_name, symbol_value):
        """
        Inserts a new symbol into the current scope.
        Args:
            symbol_type: Type of the symbol.
            symbol_name: Name of the symbol.
            symbol_value: Value of the symbol.
        """
        if self.symbolCount < MAX_SYMBOLS:
            newSymbol = self.scopeSymbolTable.symbols[self.symbolCount]
            newSymbol.name = symbol_name
            newSymbol.value = symbol_value
            newSymbol.type = symbol_type
            self.symbolCount += 1
        else:
            print("Symbol table is full")

    def symbol_exists(self, name):
        """
        Checks if a symbol exists in any of the scopes.
        Args:
            name: Name of the symbol to search for.
        Returns:
            Symbol if found, None otherwise.
        """
        currentScope = self
        while currentScope is not None:
            for i in range(currentScope.symbolCount):
                if currentScope.scopeSymbolTable.symbols[i].name == name:
                    return currentScope.scopeSymbolTable.symbols[i]
            currentScope = currentScope.nextSibling
        return None
    
    def symbol_existsInCurrent(self, name):
        """
        Checks if a symbol exists in the current scope.
        Args:
            name: Name of the symbol to search for.
        Returns:
            Symbol if found, None otherwise.
        """
        for i in range(self.symbolCount):
            if self.scopeSymbolTable.symbols[i].name == name:
                return self.scopeSymbolTable.symbols[i]
        return None


def free_environment(head):
    """
    Frees the environment by deleting all scope nodes.
    Args:
        head: The head of the scope chain.
    """
    while head is not None:
        tempNode = head
        head = head.nextSibling
        del tempNode



MAX_SYMBOLS = 100
