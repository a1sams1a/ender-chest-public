class DoWhileStmt(Stmt):
    def __init__(self, meta, cond, body):
        assert(isinstance(cond, Expr) and
               isinstance(body, Stmt))

        self.meta = meta
        self.cond = cond
        self.body = body

    def symtab(self, pos={}, order=0):
        pos['dowhile'] = pos.get('dowhile', 0) + 1

        symtabs, _, _, _ = self.body.symtab()
        if isinstance(self.body, CompoundStmt):
            return [SymTab('DOWHILE', pos['dowhile'], symtabs[0].defs, symtabs[0].symtabs), ], [], pos, order
        return [SymTab('DOWHILE', pos['dowhile'], [], symtabs), ], [], pos, order

    def __str__(self):
        body_str = str(self.body)
        if not isinstance(self.body, CompoundStmt):
            body_str = _ast_indent(body_str)

        return 'do\n%s\nwhile (%s);' % (body_str, self.cond)
