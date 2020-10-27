#código para encontrar a coluna de um token, se necessário

last_cr = self.text.rfind('\n', 0, tok.index)
        if last_cr < 0:
            last_cr = 0
        column = tok.index - last_cr
