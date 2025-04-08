import random

class Aes_128():
    def __init__(self):
        self.sbox = [
                        [int('63', 16), int('7c', 16), int('77', 16), int('7b', 16), int('f2', 16), int('6b', 16), int('6f', 16), int('c5', 16), int(
                            '30', 16), int('01', 16), int('67', 16), int('2b', 16), int('fe', 16), int('d7', 16), int('ab', 16), int('76', 16)],
                        [int('ca', 16), int('82', 16), int('c9', 16), int('7d', 16), int('fa', 16), int('59', 16), int('47', 16), int('f0', 16), int(
                            'ad', 16), int('d4', 16), int('a2', 16), int('af', 16), int('9c', 16), int('a4', 16), int('72', 16), int('c0', 16)],
                        [int('b7', 16), int('fd', 16), int('93', 16), int('26', 16), int('36', 16), int('3f', 16), int('f7', 16), int('cc', 16), int(
                            '34', 16), int('a5', 16), int('e5', 16), int('f1', 16), int('71', 16), int('d8', 16), int('31', 16), int('15', 16)],
                        [int('04', 16), int('c7', 16), int('23', 16), int('c3', 16), int('18', 16), int('96', 16), int('05', 16), int('9a', 16), int(
                            '07', 16), int('12', 16), int('80', 16), int('e2', 16), int('eb', 16), int('27', 16), int('b2', 16), int('75', 16)],
                        [int('09', 16), int('83', 16), int('2c', 16), int('1a', 16), int('1b', 16), int('6e', 16), int('5a', 16), int('a0', 16), int(
                            '52', 16), int('3b', 16), int('d6', 16), int('b3', 16), int('29', 16), int('e3', 16), int('2f', 16), int('84', 16)],
                        [int('53', 16), int('d1', 16), int('00', 16), int('ed', 16), int('20', 16), int('fc', 16), int('b1', 16), int('5b', 16), int(
                            '6a', 16), int('cb', 16), int('be', 16), int('39', 16), int('4a', 16), int('4c', 16), int('58', 16), int('cf', 16)],
                        [int('d0', 16), int('ef', 16), int('aa', 16), int('fb', 16), int('43', 16), int('4d', 16), int('33', 16), int('85', 16), int(
                            '45', 16), int('f9', 16), int('02', 16), int('7f', 16), int('50', 16), int('3c', 16), int('9f', 16), int('a8', 16)],
                        [int('51', 16), int('a3', 16), int('40', 16), int('8f', 16), int('92', 16), int('9d', 16), int('38', 16), int('f5', 16), int(
                            'bc', 16), int('b6', 16), int('da', 16), int('21', 16), int('10', 16), int('ff', 16), int('f3', 16), int('d2', 16)],
                        [int('cd', 16), int('0c', 16), int('13', 16), int('ec', 16), int('5f', 16), int('97', 16), int('44', 16), int('17', 16), int(
                            'c4', 16), int('a7', 16), int('7e', 16), int('3d', 16), int('64', 16), int('5d', 16), int('19', 16), int('73', 16)],
                        [int('60', 16), int('81', 16), int('4f', 16), int('dc', 16), int('22', 16), int('2a', 16), int('90', 16), int('88', 16), int(
                            '46', 16), int('ee', 16), int('b8', 16), int('14', 16), int('de', 16), int('5e', 16), int('0b', 16), int('db', 16)],
                        [int('e0', 16), int('32', 16), int('3a', 16), int('0a', 16), int('49', 16), int('06', 16), int('24', 16), int('5c', 16), int(
                            'c2', 16), int('d3', 16), int('ac', 16), int('62', 16), int('91', 16), int('95', 16), int('e4', 16), int('79', 16)],
                        [int('e7', 16), int('c8', 16), int('37', 16), int('6d', 16), int('8d', 16), int('d5', 16), int('4e', 16), int('a9', 16), int(                                '6c', 16), int('56', 16), int('f4', 16), int('ea', 16), int('65', 16), int('7a', 16), int('ae', 16), int('08', 16)],
                        [int('ba', 16), int('78', 16), int('25', 16), int('2e', 16), int('1c', 16), int('a6', 16), int('b4', 16), int('c6', 16), int(
                            'e8', 16), int('dd', 16), int('74', 16), int('1f', 16), int('4b', 16), int('bd', 16), int('8b', 16), int('8a', 16)],
                        [int('70', 16), int('3e', 16), int('b5', 16), int('66', 16), int('48', 16), int('03', 16), int('f6', 16), int('0e', 16), int(
                            '61', 16), int('35', 16), int('57', 16), int('b9', 16), int('86', 16), int('c1', 16), int('1d', 16), int('9e', 16)],
                        [int('e1', 16), int('f8', 16), int('98', 16), int('11', 16), int('69', 16), int('d9', 16), int('8e', 16), int('94', 16), int(
                            '9b', 16), int('1e', 16), int('87', 16), int('e9', 16), int('ce', 16), int('55', 16), int('28', 16), int('df', 16)],
                        [int('8c', 16), int('a1', 16), int('89', 16), int('0d', 16), int('bf', 16), int('e6', 16), int('42', 16), int('68', 16), int(
                            '41', 16), int('99', 16), int('2d', 16), int('0f', 16), int('b0', 16), int('54', 16), int('bb', 16), int('16', 16)]
        ]
        
        self.rev_sbox = [
                            [int('52', 16), int('09', 16), int('6a', 16), int('d5', 16), int('30', 16), int('36', 16), int('a5', 16), int('38', 16), int(
                                'bf', 16), int('40', 16), int('a3', 16), int('9e', 16), int('81', 16), int('f3', 16), int('d7', 16), int('fb', 16)],
                            [int('7c', 16), int('e3', 16), int('39', 16), int('82', 16), int('9b', 16), int('2f', 16), int('ff', 16), int('87', 16), int(
                                '34', 16), int('8e', 16), int('43', 16), int('44', 16), int('c4', 16), int('de', 16), int('e9', 16), int('cb', 16)],
                            [int('54', 16), int('7b', 16), int('94', 16), int('32', 16), int('a6', 16), int('c2', 16), int('23', 16), int('3d', 16), int(
                                'ee', 16), int('4c', 16), int('95', 16), int('0b', 16), int('42', 16), int('fa', 16), int('c3', 16), int('4e', 16)],
                            [int('08', 16), int('2e', 16), int('a1', 16), int('66', 16), int('28', 16), int('d9', 16), int('24', 16), int('b2', 16), int(
                                '76', 16), int('5b', 16), int('a2', 16), int('49', 16), int('6d', 16), int('8b', 16), int('d1', 16), int('25', 16)],
                            [int('72', 16), int('f8', 16), int('f6', 16), int('64', 16), int('86', 16), int('68', 16), int('98', 16), int('16', 16), int(
                                'd4', 16), int('a4', 16), int('5c', 16), int('cc', 16), int('5d', 16), int('65', 16), int('b6', 16), int('92', 16)],
                            [int('6c', 16), int('70', 16), int('48', 16), int('50', 16), int('fd', 16), int('ed', 16), int('b9', 16), int('da', 16), int(
                                '5e', 16), int('15', 16), int('46', 16), int('57', 16), int('a7', 16), int('8d', 16), int('9d', 16), int('84', 16)],
                            [int('90', 16), int('d8', 16), int('ab', 16), int('00', 16), int('8c', 16), int('bc', 16), int('d3', 16), int('0a', 16), int(
                                'f7', 16), int('e4', 16), int('58', 16), int('05', 16), int('b8', 16), int('b3', 16), int('45', 16), int('06', 16)],
                            [int('d0', 16), int('2c', 16), int('1e', 16), int('8f', 16), int('ca', 16), int('3f', 16), int('0f', 16), int('02', 16), int(
                                'c1', 16), int('af', 16), int('bd', 16), int('03', 16), int('01', 16), int('13', 16), int('8a', 16), int('6b', 16)],
                            [int('3a', 16), int('91', 16), int('11', 16), int('41', 16), int('4f', 16), int('67', 16), int('dc', 16), int('ea', 16), int(
                                '97', 16), int('f2', 16), int('cf', 16), int('ce', 16), int('f0', 16), int('b4', 16), int('e6', 16), int('73', 16)],
                            [int('96', 16), int('ac', 16), int('74', 16), int('22', 16), int('e7', 16), int('ad', 16), int('35', 16), int('85', 16), int(
                                'e2', 16), int('f9', 16), int('37', 16), int('e8', 16), int('1c', 16), int('75', 16), int('df', 16), int('6e', 16)],
                            [int('47', 16), int('f1', 16), int('1a', 16), int('71', 16), int('1d', 16), int('29', 16), int('c5', 16), int('89', 16), int(
                                '6f', 16), int('b7', 16), int('62', 16), int('0e', 16), int('aa', 16), int('18', 16), int('be', 16), int('1b', 16)],
                            [int('fc', 16), int('56', 16), int('3e', 16), int('4b', 16), int('c6', 16), int('d2', 16), int('79', 16), int('20', 16), int(
                                '9a', 16), int('db', 16), int('c0', 16), int('fe', 16), int('78', 16), int('cd', 16), int('5a', 16), int('f4', 16)],
                            [int('1f', 16), int('dd', 16), int('a8', 16), int('33', 16), int('88', 16), int('07', 16), int('c7', 16), int('31', 16), int(
                                'b1', 16), int('12', 16), int('10', 16), int('59', 16), int('27', 16), int('80', 16), int('ec', 16), int('5f', 16)],
                            [int('60', 16), int('51', 16), int('7f', 16), int('a9', 16), int('19', 16), int('b5', 16), int('4a', 16), int('0d', 16), int(
                                '2d', 16), int('e5', 16), int('7a', 16), int('9f', 16), int('93', 16), int('c9', 16), int('9c', 16), int('ef', 16)],
                            [int('a0', 16), int('e0', 16), int('3b', 16), int('4d', 16), int('ae', 16), int('2a', 16), int('f5', 16), int('b0', 16), int(
                                'c8', 16), int('eb', 16), int('bb', 16), int('3c', 16), int('83', 16), int('53', 16), int('99', 16), int('61', 16)],
                            [int('17', 16), int('2b', 16), int('04', 16), int('7e', 16), int('ba', 16), int('77', 16), int('d6', 16), int('26', 16), int(
                                'e1', 16), int('69', 16), int('14', 16), int('63', 16), int('55', 16), int('21', 16), int('0c', 16), int('7d', 16)]
        ]
        
    def visualizar(self, dado):
        x = dado >> 4
        y = dado & 15
        return self.sbox[x][y]

    def visualizar_reverse(self, dado):
        x = dado >> 4
        y = dado & 15
        return self.rev_sbox[x][y]

    def Rotacionar_Esq(self, row, n=1):
        return row[n:] + row[:n]

    def break_in_grids_of_16(self, s):
        lista_temp = []
        for i in range(len(s) // 16):
            b = s[i * 16: i * 16 + 16]
            grade = [list(b[i * 4:i * 4 + 4]) for i in range(4)]
            lista_temp.append(grade)
        return lista_temp

    def Expansao_Chave(self, chave, num_rodadas):
        rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

        while len(rcon) < num_rodadas:
            rcon.append(self.multiplicar_2(rcon[-1]))

        chave_expandida = [list(chave[i:i + 4]) for i in range(0, 16, 4)]

        for i in range(4, (num_rodadas + 1) * 4):
            temp = chave_expandida[i - 1]
            if i % 4 == 0:
                temp = self.Rotacionar_Esq(temp)
                temp = [self.visualizar(b) for b in temp]
                temp[0] ^= rcon[i // 4 - 1]
            chave_expandida.append([a ^ b for a, b in zip(chave_expandida[i - 4], temp)])

        return chave_expandida

    def multiplicar_2(self, valor):
        temp = valor << 1
        temp &= 0xff
        if (valor & 128) != 0:
            temp ^= 0x1b
        return temp

    def multiplicar_3(self, valor):
        return self.multiplicar_2(valor) ^ valor
    
    def multiplicar_9(self, valor):
        return self.multiplicar_2(self.multiplicar_2(self.multiplicar_2(valor))) ^ valor

    def multiplicar_11(self, valor):
        return self.multiplicar_2(self.multiplicar_2(self.multiplicar_2(valor)) ^ valor) ^ valor

    def multiplicar_13(self, valor):
        return self.multiplicar_2(self.multiplicar_2(self.multiplicar_2(valor) ^ valor)) ^ valor

    def multiplicar_14(self, valor):
        return self.multiplicar_2(self.multiplicar_2(self.multiplicar_2(valor) ^ valor) ^ valor)

    def misturarColuna(self, coluna):
        return [
            self.multiplicar_2(coluna[0]) ^ self.multiplicar_3(coluna[1]) ^ coluna[2] ^ coluna[3],
            self.multiplicar_2(coluna[1]) ^ self.multiplicar_3(coluna[2]) ^ coluna[3] ^ coluna[0],
            self.multiplicar_2(coluna[2]) ^ self.multiplicar_3(coluna[3]) ^ coluna[0] ^ coluna[1],
            self.multiplicar_2(coluna[3]) ^ self.multiplicar_3(coluna[0]) ^ coluna[1] ^ coluna[2]
        ]

    def misturar_colunas(self, grade):
        nova_grade = [[], [], [], []]
        for numero in range(4):
            coluna = [grade[coluna][numero] for coluna in range(4)]
            coluna = self.misturarColuna(coluna)
            for column in range(4):
                nova_grade[column].append(coluna[column])
        return nova_grade
    def inverse_misturar_colunas(self, grade):
        nova_grade = [[], [], [], []]
        for numero in range(4):
            coluna = [grade[coluna][numero] for coluna in range(4)]
            coluna = self.inverse_misturarColuna(coluna)
            for column in range(4):
                nova_grade[column].append(coluna[column])
        return nova_grade

    def inverse_misturarColuna(self, coluna):
        matriz = [
            self.multiplicar_14(coluna[0]) ^ self.multiplicar_11(coluna[1]) ^ self.multiplicar_13(coluna[2]) ^ self.multiplicar_9(coluna[3]),
            self.multiplicar_9(coluna[0]) ^ self.multiplicar_14(coluna[1]) ^ self.multiplicar_11(coluna[2]) ^ self.multiplicar_13(coluna[3]),
            self.multiplicar_13(coluna[0]) ^ self.multiplicar_9(coluna[1]) ^ self.multiplicar_14(coluna[2]) ^ self.multiplicar_11(coluna[3]),
            self.multiplicar_11(coluna[0]) ^ self.multiplicar_13(coluna[1]) ^ self.multiplicar_9(coluna[2]) ^ self.multiplicar_14(coluna[3])
        ]
        return matriz

    def addicionarSubKey(self, bloco, chave):
        return [[b ^ k for b, k in zip(row_b, row_k)] for row_b, row_k in zip(bloco, chave)]

    def encriptar(self, chave, dado, num_rodadas):
        if len(chave) != 16:
            raise ValueError("A chave deve ter 16 bytes (128 bits).")

        if isinstance(dado, str):
            dado = dado.encode()

        # Padding
        pad_length = 16 - (len(dado) % 16)
        dado += bytes([pad_length] * pad_length)

        grades = self.break_in_grids_of_16(dado)
        chave_expandida = self.Expansao_Chave(chave, num_rodadas)

        for i, grade in enumerate(grades):
            grade = self.addicionarSubKey(grade, chave_expandida[:4])
            for rodada in range(1, num_rodadas):
                grade = [[self.visualizar(b) for b in row] for row in grade]
                grade = [self.Rotacionar_Esq(row) for row in grade]
                grade = self.misturar_colunas(grade)
                grade = self.addicionarSubKey(grade, chave_expandida[rodada * 4:(rodada + 1) * 4])
            grade = [[self.visualizar(b) for b in row] for row in grade]
            grade = [self.Rotacionar_Esq(row) for row in grade]
            grade = self.addicionarSubKey(grade, chave_expandida[num_rodadas * 4:])
            grades[i] = grade

        return b''.join([bytes([b for row in grade for b in row]) for grade in grades])

    def decriptar(self, chave, dado, num_rodadas):
        if isinstance(dado, str):
            dado = dado.encode()

        grades = self.break_in_grids_of_16(dado)
        chave_expandida = self.Expansao_Chave(chave, num_rodadas)

        for i, grade in enumerate(grades):
            grade = self.addicionarSubKey(grade, chave_expandida[num_rodadas * 4:])
            grade = [self.Rotacionar_Esq(row, -1) for row in grade]
            grade = [[self.visualizar_reverse(b) for b in row] for row in grade]

            for rodada in range(num_rodadas - 1, 0, -1):
                grade = self.addicionarSubKey(grade, chave_expandida[rodada * 4:(rodada + 1) * 4])
                grade = self.inverse_misturar_colunas(grade)  # Inverse MixColumns
                grade = [self.Rotacionar_Esq(row, -1) for row in grade]
                grade = [[self.visualizar_reverse(b) for b in row] for row in grade]

            grade = self.addicionarSubKey(grade, chave_expandida[:4])
            grades[i] = grade

        decrypted_bytes = b''.join([bytes([b for row in grade for b in row]) for grade in grades])

        # Remover o padding
        if decrypted_bytes:
            pad_length = decrypted_bytes[-1]
            if 0 < pad_length <= 16:
                decrypted_bytes = decrypted_bytes[:-pad_length]

        return decrypted_bytes