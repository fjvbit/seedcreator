#import mnemonic
import random
import binascii
import hashlib

from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QApplication, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox

from PySide2.QtGui import QIntValidator

from ui import mainui

class TRangeError(Exception):
    pass


class TMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =mainui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.onlyInt = QIntValidator()
        #self.onlyInt.setRange(1,16)

        # word 1
        self.ui.lew1w1.setValidator(self.onlyInt)
        self.ui.lew1w2.setValidator(self.onlyInt)
        self.ui.lew1w3.setValidator(self.onlyInt)

        # word 2
        self.ui.lew2w1.setValidator(self.onlyInt)
        self.ui.lew2w2.setValidator(self.onlyInt)
        self.ui.lew2w3.setValidator(self.onlyInt)

        # word 3
        self.ui.lew3w1.setValidator(self.onlyInt)
        self.ui.lew3w2.setValidator(self.onlyInt)
        self.ui.lew3w3.setValidator(self.onlyInt)

        # word 4
        self.ui.lew4w1.setValidator(self.onlyInt)
        self.ui.lew4w2.setValidator(self.onlyInt)
        self.ui.lew4w3.setValidator(self.onlyInt)

        # word 5
        self.ui.lew5w1.setValidator(self.onlyInt)
        self.ui.lew5w2.setValidator(self.onlyInt)
        self.ui.lew5w3.setValidator(self.onlyInt)

        # word 6
        self.ui.lew6w1.setValidator(self.onlyInt)
        self.ui.lew6w2.setValidator(self.onlyInt)
        self.ui.lew6w3.setValidator(self.onlyInt)

        # word 7
        self.ui.lew7w1.setValidator(self.onlyInt)
        self.ui.lew7w2.setValidator(self.onlyInt)
        self.ui.lew7w3.setValidator(self.onlyInt)

        # word 8
        self.ui.lew8w1.setValidator(self.onlyInt)
        self.ui.lew8w2.setValidator(self.onlyInt)
        self.ui.lew8w3.setValidator(self.onlyInt)

        # word 9
        self.ui.lew9w1.setValidator(self.onlyInt)
        self.ui.lew9w2.setValidator(self.onlyInt)
        self.ui.lew9w3.setValidator(self.onlyInt)

        # word 10
        self.ui.lew10w1.setValidator(self.onlyInt)
        self.ui.lew10w2.setValidator(self.onlyInt)
        self.ui.lew10w3.setValidator(self.onlyInt)

        # word 11
        self.ui.lew11w1.setValidator(self.onlyInt)
        self.ui.lew11w2.setValidator(self.onlyInt)
        self.ui.lew11w3.setValidator(self.onlyInt)

        # word 12
        self.ui.lew12w1.setValidator(self.onlyInt)
        self.ui.lew12w2.setValidator(self.onlyInt)
        self.ui.lew12w3.setValidator(self.onlyInt)

        # word 13
        self.ui.lew13w1.setValidator(self.onlyInt)
        self.ui.lew13w2.setValidator(self.onlyInt)
        self.ui.lew13w3.setValidator(self.onlyInt)

        # word 14
        self.ui.lew14w1.setValidator(self.onlyInt)
        self.ui.lew14w2.setValidator(self.onlyInt)
        self.ui.lew14w3.setValidator(self.onlyInt)

        # word 15
        self.ui.lew15w1.setValidator(self.onlyInt)
        self.ui.lew15w2.setValidator(self.onlyInt)
        self.ui.lew15w3.setValidator(self.onlyInt)

        # word 16
        self.ui.lew16w1.setValidator(self.onlyInt)
        self.ui.lew16w2.setValidator(self.onlyInt)
        self.ui.lew16w3.setValidator(self.onlyInt)

        # word 17
        self.ui.lew17w1.setValidator(self.onlyInt)
        self.ui.lew17w2.setValidator(self.onlyInt)
        self.ui.lew17w3.setValidator(self.onlyInt)

        # word 18
        self.ui.lew18w1.setValidator(self.onlyInt)
        self.ui.lew18w2.setValidator(self.onlyInt)
        self.ui.lew18w3.setValidator(self.onlyInt)

        # word 19
        self.ui.lew19w1.setValidator(self.onlyInt)
        self.ui.lew19w2.setValidator(self.onlyInt)
        self.ui.lew19w3.setValidator(self.onlyInt)

        # word 20
        self.ui.lew20w1.setValidator(self.onlyInt)
        self.ui.lew20w2.setValidator(self.onlyInt)
        self.ui.lew20w3.setValidator(self.onlyInt)

        # word 21
        self.ui.lew21w1.setValidator(self.onlyInt)
        self.ui.lew21w2.setValidator(self.onlyInt)
        self.ui.lew21w3.setValidator(self.onlyInt)

        # word 22
        self.ui.lew22w1.setValidator(self.onlyInt)
        self.ui.lew22w2.setValidator(self.onlyInt)
        self.ui.lew22w3.setValidator(self.onlyInt)

        # word 23
        self.ui.lew23w1.setValidator(self.onlyInt)
        self.ui.lew23w2.setValidator(self.onlyInt)
        self.ui.lew23w3.setValidator(self.onlyInt)


        self.ui.pBCalculate.clicked.connect(self.buttonCalculate)
        self.ui.pBClear.clicked.connect(self.clearForm)
        self.ui.pBRandom.clicked.connect(self.calcRandom)
        self.ui.pPBCreateHash.clicked.connect(self.createHash)
        self.ui.pPBCreateHash.hide()
        self.clearForm()
        self.readWortList()

    def createHash3(self):
        wuerfel24 = (int(self.ui.lew24w1.text()) -1 )// 2
        bit24 = bin(wuerfel24)[2:].zfill(3)
        b = self.b + bit24
        l = len(b)
        print ("Lanege:", l)
        bint = int(b, 2)
        bhex = hex(bint)[2:]
        bhex = bhex.zfill(32)
        uhex = binascii.unhexlify(bhex)
        l2 = len(uhex)
        byt = uhex
        nd = byt.zfill((l//33*8))
        l3 = len(nd)

        hash = hashlib.sha256(byt)
        hash2 = hashlib.sha256(nd)
        hexhash = hash.hexdigest()
        hexhash2 = hash.hexdigest()
        inthash = int(hexhash,16)
        binhash = (bin(inthash)[2:]).zfill(256)
        l4 = len(binhash)
        endbin = binhash[:8]

        lastNumber = bit24 + endbin
        lastIndex = int(lastNumber, 2)



        print("wuerfel24: ", wuerfel24, bin(wuerfel24)[2:])
        print ("Index", lastIndex)

    def createHash(self):
        wuerfel24 = (int(self.ui.lew24w1.text()) -1 )// 2
        bit24 = bin(wuerfel24)[2:].zfill(3)
        b = self.b + bit24
        bint = int(b, 2)
        bhex = hex(bint)[2:].zfill(64)
        byteStr = binascii.unhexlify(bhex)

        hash = hashlib.sha256(byteStr)
        hexhash = hash.hexdigest()
        inthash = int(hexhash,16)
        binhash = (bin(inthash)[2:]).zfill(256)
        endbin = binhash[:8]

        lastNumber = bit24 + endbin
        lastIndex = int(lastNumber,2)

        #print ("Index", lastIndex)
        return lastIndex


    # check additional word for seed
    def __check_seed(self, index):
        b = self.b + bin(index)[2:].zfill(11)
        l = len(b)  # noqa: E741
        d = b[: l // 33 * 32]
        h = b[-l // 33 :]
        nd = binascii.unhexlify(hex(int(d, 2))[2:].rstrip("L").zfill(l // 33 * 8))
        nh = bin(int(hashlib.sha256(nd).hexdigest(), 16))[2:].zfill(256)[: l // 33]
        return h == nh


    def __find_word24_all(self):
        l = []
        for i in range (0, len(self.wortliste)):
            if self.__check_seed(i):
                word = self.wortliste[i]
                print ('Gefunden 2', i, word)
                l.append(i)
        print (' ')
        return l

    def __find_word24(self):
        for i in range (0, len(self.wortliste)):
            if self.__check_seed(i):
                word = self.wortliste[i]
                print ('Gefunden 2', i, word)
                self.ui.labelWort24.setText(word)
                self.seed += word
                return True
        print ('nicht gefunden')
        return False


    # def __find_word24_2(self):
    #     m = mnemonic.Mnemonic('english')
    #     for word in self.wortliste:
    #         check = self.seed + word
    #         if m.check(check):
    #             print ('Gefunden', word)
    #             self.ui.labelWort24.setText(word)
    #             self.seed = check
    #             return True
    #     print ('nicht gefunden')
    #     return False

    def calcRandom(self):
        self.ui.lew1w1.setText(str(random.randint(1, 16)))
        self.ui.lew1w2.setText(str(random.randint(1, 16)))
        self.ui.lew1w3.setText(str(random.randint(1, 16)))

        self.ui.lew2w1.setText(str(random.randint(1, 16)))
        self.ui.lew2w2.setText(str(random.randint(1, 16)))
        self.ui.lew2w3.setText(str(random.randint(1, 16)))

        self.ui.lew3w1.setText(str(random.randint(1, 16)))
        self.ui.lew3w2.setText(str(random.randint(1, 16)))
        self.ui.lew3w3.setText(str(random.randint(1, 16)))

        self.ui.lew4w1.setText(str(random.randint(1, 16)))
        self.ui.lew4w2.setText(str(random.randint(1, 16)))
        self.ui.lew4w3.setText(str(random.randint(1, 16)))

        self.ui.lew5w1.setText(str(random.randint(1, 16)))
        self.ui.lew5w2.setText(str(random.randint(1, 16)))
        self.ui.lew5w3.setText(str(random.randint(1, 16)))

        self.ui.lew6w1.setText(str(random.randint(1, 16)))
        self.ui.lew6w2.setText(str(random.randint(1, 16)))
        self.ui.lew6w3.setText(str(random.randint(1, 16)))

        self.ui.lew7w1.setText(str(random.randint(1, 16)))
        self.ui.lew7w2.setText(str(random.randint(1, 16)))
        self.ui.lew7w3.setText(str(random.randint(1, 16)))

        self.ui.lew8w1.setText(str(random.randint(1, 16)))
        self.ui.lew8w2.setText(str(random.randint(1, 16)))
        self.ui.lew8w3.setText(str(random.randint(1, 16)))

        self.ui.lew9w1.setText(str(random.randint(1, 16)))
        self.ui.lew9w2.setText(str(random.randint(1, 16)))
        self.ui.lew9w3.setText(str(random.randint(1, 16)))

        self.ui.lew10w1.setText(str(random.randint(1, 16)))
        self.ui.lew10w2.setText(str(random.randint(1, 16)))
        self.ui.lew10w3.setText(str(random.randint(1, 16)))

        self.ui.lew11w1.setText(str(random.randint(1, 16)))
        self.ui.lew11w2.setText(str(random.randint(1, 16)))
        self.ui.lew11w3.setText(str(random.randint(1, 16)))

        self.ui.lew12w1.setText(str(random.randint(1, 16)))
        self.ui.lew12w2.setText(str(random.randint(1, 16)))
        self.ui.lew12w3.setText(str(random.randint(1, 16)))

        self.ui.lew13w1.setText(str(random.randint(1, 16)))
        self.ui.lew13w2.setText(str(random.randint(1, 16)))
        self.ui.lew13w3.setText(str(random.randint(1, 16)))

        self.ui.lew14w1.setText(str(random.randint(1, 16)))
        self.ui.lew14w2.setText(str(random.randint(1, 16)))
        self.ui.lew14w3.setText(str(random.randint(1, 16)))

        self.ui.lew15w1.setText(str(random.randint(1, 16)))
        self.ui.lew15w2.setText(str(random.randint(1, 16)))
        self.ui.lew15w3.setText(str(random.randint(1, 16)))

        self.ui.lew16w1.setText(str(random.randint(1, 16)))
        self.ui.lew16w2.setText(str(random.randint(1, 16)))
        self.ui.lew16w3.setText(str(random.randint(1, 16)))

        self.ui.lew17w1.setText(str(random.randint(1, 16)))
        self.ui.lew17w2.setText(str(random.randint(1, 16)))
        self.ui.lew17w3.setText(str(random.randint(1, 16)))

        self.ui.lew18w1.setText(str(random.randint(1, 16)))
        self.ui.lew18w2.setText(str(random.randint(1, 16)))
        self.ui.lew18w3.setText(str(random.randint(1, 16)))

        self.ui.lew19w1.setText(str(random.randint(1, 16)))
        self.ui.lew19w2.setText(str(random.randint(1, 16)))
        self.ui.lew19w3.setText(str(random.randint(1, 16)))

        self.ui.lew20w1.setText(str(random.randint(1, 16)))
        self.ui.lew20w2.setText(str(random.randint(1, 16)))
        self.ui.lew20w3.setText(str(random.randint(1, 16)))

        self.ui.lew21w1.setText(str(random.randint(1, 16)))
        self.ui.lew21w2.setText(str(random.randint(1, 16)))
        self.ui.lew21w3.setText(str(random.randint(1, 16)))

        self.ui.lew22w1.setText(str(random.randint(1, 16)))
        self.ui.lew22w2.setText(str(random.randint(1, 16)))
        self.ui.lew22w3.setText(str(random.randint(1, 16)))

        self.ui.lew23w1.setText(str(random.randint(1, 16)))
        self.ui.lew23w2.setText(str(random.randint(1, 16)))
        self.ui.lew23w3.setText(str(random.randint(1, 16)))

        self.ui.lew24w1.setText(str(random.randint(1, 16)))


        self.buttonCalculate()

        #self.__find_word24()


    def clearForm(self):

        self.seed = ''
        self.ui.lew1w1.setText('')
        self.ui.lew1w2.setText('')
        self.ui.lew1w3.setText('')

        self.ui.lew2w1.setText('')
        self.ui.lew2w2.setText('')
        self.ui.lew2w3.setText('')

        self.ui.lew3w1.setText('')
        self.ui.lew3w2.setText('')
        self.ui.lew3w3.setText('')

        self.ui.lew4w1.setText('')
        self.ui.lew4w2.setText('')
        self.ui.lew4w3.setText('')

        self.ui.lew5w1.setText('')
        self.ui.lew5w2.setText('')
        self.ui.lew5w3.setText('')

        self.ui.lew6w1.setText('')
        self.ui.lew6w2.setText('')
        self.ui.lew6w3.setText('')

        self.ui.lew7w1.setText('')
        self.ui.lew7w2.setText('')
        self.ui.lew7w3.setText('')

        self.ui.lew8w1.setText('')
        self.ui.lew8w2.setText('')
        self.ui.lew8w3.setText('')

        self.ui.lew9w1.setText('')
        self.ui.lew9w2.setText('')
        self.ui.lew9w3.setText('')

        self.ui.lew10w1.setText('')
        self.ui.lew10w2.setText('')
        self.ui.lew10w3.setText('')

        self.ui.lew11w1.setText('')
        self.ui.lew11w2.setText('')
        self.ui.lew11w3.setText('')

        self.ui.lew12w1.setText('')
        self.ui.lew12w2.setText('')
        self.ui.lew12w3.setText('')

        self.ui.lew13w1.setText('')
        self.ui.lew13w2.setText('')
        self.ui.lew13w3.setText('')

        self.ui.lew14w1.setText('')
        self.ui.lew14w2.setText('')
        self.ui.lew14w3.setText('')

        self.ui.lew15w1.setText('')
        self.ui.lew15w2.setText('')
        self.ui.lew15w3.setText('')

        self.ui.lew16w1.setText('')
        self.ui.lew16w2.setText('')
        self.ui.lew16w3.setText('')

        self.ui.lew17w1.setText('')
        self.ui.lew17w2.setText('')
        self.ui.lew17w3.setText('')

        self.ui.lew18w1.setText('')
        self.ui.lew18w2.setText('')
        self.ui.lew18w3.setText('')

        self.ui.lew19w1.setText('')
        self.ui.lew19w2.setText('')
        self.ui.lew19w3.setText('')

        self.ui.lew20w1.setText('')
        self.ui.lew20w2.setText('')
        self.ui.lew20w3.setText('')

        self.ui.lew21w1.setText('')
        self.ui.lew21w2.setText('')
        self.ui.lew21w3.setText('')

        self.ui.lew22w1.setText('')
        self.ui.lew22w2.setText('')
        self.ui.lew22w3.setText('')

        self.ui.lew23w1.setText('')
        self.ui.lew23w2.setText('')
        self.ui.lew23w3.setText('')

        self.ui.lew24w1.setText('')


        self.ui.labelWort1Index.setText('')
        self.ui.labelWort2Index.setText('')
        self.ui.labelWort3Index.setText('')
        self.ui.labelWort4Index.setText('')
        self.ui.labelWort5Index.setText('')
        self.ui.labelWort6Index.setText('')
        self.ui.labelWort7Index.setText('')
        self.ui.labelWort8Index.setText('')
        self.ui.labelWort9Index.setText('')
        self.ui.labelWort10Index.setText('')
        self.ui.labelWort11Index.setText('')
        self.ui.labelWort12Index.setText('')
        self.ui.labelWort13Index.setText('')
        self.ui.labelWort14Index.setText('')
        self.ui.labelWort15Index.setText('')
        self.ui.labelWort16Index.setText('')
        self.ui.labelWort17Index.setText('')
        self.ui.labelWort18Index.setText('')
        self.ui.labelWort19Index.setText('')
        self.ui.labelWort20Index.setText('')
        self.ui.labelWort21Index.setText('')
        self.ui.labelWort22Index.setText('')
        self.ui.labelWort23Index.setText('')
        self.ui.labelWort24Index.setText('')


        self.ui.labelWort1.setText('')
        self.ui.labelWort2.setText('')
        self.ui.labelWort3.setText('')
        self.ui.labelWort4.setText('')
        self.ui.labelWort5.setText('')
        self.ui.labelWort6.setText('')
        self.ui.labelWort7.setText('')
        self.ui.labelWort8.setText('')
        self.ui.labelWort9.setText('')
        self.ui.labelWort10.setText('')
        self.ui.labelWort11.setText('')
        self.ui.labelWort12.setText('')
        self.ui.labelWort13.setText('')
        self.ui.labelWort14.setText('')
        self.ui.labelWort15.setText('')
        self.ui.labelWort16.setText('')
        self.ui.labelWort17.setText('')
        self.ui.labelWort18.setText('')
        self.ui.labelWort19.setText('')
        self.ui.labelWort20.setText('')
        self.ui.labelWort21.setText('')
        self.ui.labelWort22.setText('')
        self.ui.labelWort23.setText('')
        self.ui.labelWort24.setText('')
        self.ui.textEditSeed.setText('')


    def getIndex(self, zahl1, zahl2, zahl3):
        if (zahl1 < 1 or zahl1 > 16 or zahl2 < 1 or zahl2 > 16 or zahl3 < 1 or zahl3 > 16 ):
            raise TRangeError("Eingaben nicht im richtigen Bereich (1-16)")
        val = ((zahl1 - 1)*256 + (zahl2 - 1) * 16 + zahl3 - 1) // 2
        return val

    def __calulate(self, le1, le2, le3, labelIndex, labelWort):
        t1 = le1.text()
        t2 = le2.text()
        t3 = le3.text()
        if t1 == '' or t2 == '' or t3 == '':
            labelIndex.setText('')
            labelWort.setText('')
            return
        try:
            z1 = int(t1)
            z2 = int(t2)
            z3 = int(t3)
            index = self.getIndex(z1, z2, z3)
            #index List erstellen
            self.indexList.append(index)
            self.b += bin(index)[2:].zfill(11)
        except:
            labelIndex.setText('')
            labelWort.setText('')
            return
        labelIndex.setText(str(index))
        labelWort.setText(self.wortliste[index])
        self.seed += self.wortliste[index] + ' '


    def buttonCalculate2(self):
        # Werte initialisieren
        self.seed = ''
        self.indexList = []
        self.b = ''
        self.__calulate(self.ui.lew1w1, self.ui.lew1w2, self.ui.lew1w3, self.ui.labelWort1Index, self.ui.labelWort1)
        self.__calulate(self.ui.lew2w1, self.ui.lew2w2, self.ui.lew2w3, self.ui.labelWort2Index, self.ui.labelWort2)
        self.__calulate(self.ui.lew3w1, self.ui.lew3w2, self.ui.lew3w3, self.ui.labelWort3Index, self.ui.labelWort3)
        self.__calulate(self.ui.lew4w1, self.ui.lew4w2, self.ui.lew4w3, self.ui.labelWort4Index, self.ui.labelWort4)
        self.__calulate(self.ui.lew5w1, self.ui.lew5w2, self.ui.lew5w3, self.ui.labelWort5Index, self.ui.labelWort5)
        self.__calulate(self.ui.lew6w1, self.ui.lew6w2, self.ui.lew6w3, self.ui.labelWort6Index, self.ui.labelWort6)
        self.__calulate(self.ui.lew7w1, self.ui.lew7w2, self.ui.lew7w3, self.ui.labelWort7Index, self.ui.labelWort7)
        self.__calulate(self.ui.lew8w1, self.ui.lew8w2, self.ui.lew8w3, self.ui.labelWort8Index, self.ui.labelWort8)
        self.__calulate(self.ui.lew9w1, self.ui.lew9w2, self.ui.lew9w3, self.ui.labelWort9Index, self.ui.labelWort9)
        self.__calulate(self.ui.lew10w1, self.ui.lew10w2, self.ui.lew10w3, self.ui.labelWort10Index, self.ui.labelWort10)
        self.__calulate(self.ui.lew11w1, self.ui.lew11w2, self.ui.lew11w3, self.ui.labelWort11Index, self.ui.labelWort11)
        self.__calulate(self.ui.lew12w1, self.ui.lew12w2, self.ui.lew12w3, self.ui.labelWort12Index, self.ui.labelWort12)
        self.__calulate(self.ui.lew13w1, self.ui.lew13w2, self.ui.lew13w3, self.ui.labelWort13Index, self.ui.labelWort13)
        self.__calulate(self.ui.lew14w1, self.ui.lew14w2, self.ui.lew14w3, self.ui.labelWort14Index, self.ui.labelWort14)
        self.__calulate(self.ui.lew15w1, self.ui.lew15w2, self.ui.lew15w3, self.ui.labelWort15Index, self.ui.labelWort15)
        self.__calulate(self.ui.lew16w1, self.ui.lew16w2, self.ui.lew16w3, self.ui.labelWort16Index, self.ui.labelWort16)
        self.__calulate(self.ui.lew17w1, self.ui.lew17w2, self.ui.lew17w3, self.ui.labelWort17Index, self.ui.labelWort17)
        self.__calulate(self.ui.lew18w1, self.ui.lew18w2, self.ui.lew18w3, self.ui.labelWort18Index, self.ui.labelWort18)
        self.__calulate(self.ui.lew19w1, self.ui.lew19w2, self.ui.lew19w3, self.ui.labelWort19Index, self.ui.labelWort19)
        self.__calulate(self.ui.lew20w1, self.ui.lew20w2, self.ui.lew20w3, self.ui.labelWort20Index, self.ui.labelWort20)
        self.__calulate(self.ui.lew21w1, self.ui.lew21w2, self.ui.lew21w3, self.ui.labelWort21Index, self.ui.labelWort21)
        self.__calulate(self.ui.lew22w1, self.ui.lew22w2, self.ui.lew22w3, self.ui.labelWort22Index, self.ui.labelWort22)
        self.__calulate(self.ui.lew23w1, self.ui.lew23w2, self.ui.lew23w3, self.ui.labelWort23Index, self.ui.labelWort23)

        self.w24Liste = self.__find_word24_all()
        l = len(self.b)
        b2 = self.b

        print ("Laenge", l,b2)

        if len(self.w24Liste) == 8:
            try:
                wuerfel24 = int(self.ui.lew24w1.text())
                index = self.w24Liste[(wuerfel24-1) // 2]
                word = self.wortliste[index]
                self.ui.labelWort24.setText(word)
                self.ui.labelWort24Index.setText(str(index))
                self.seed += word
            except:
                self.seed = ''
                self.ui.labelWort24.setText('')

        else:
            self.seed = ''


        #self.__find_word24()

        self.ui.textEditSeed.setText(self.seed)


    def buttonCalculate(self):
        # Werte initialisieren
        self.seed = ''
        self.indexList = []
        self.b = ''
        self.__calulate(self.ui.lew1w1, self.ui.lew1w2, self.ui.lew1w3, self.ui.labelWort1Index, self.ui.labelWort1)
        self.__calulate(self.ui.lew2w1, self.ui.lew2w2, self.ui.lew2w3, self.ui.labelWort2Index, self.ui.labelWort2)
        self.__calulate(self.ui.lew3w1, self.ui.lew3w2, self.ui.lew3w3, self.ui.labelWort3Index, self.ui.labelWort3)
        self.__calulate(self.ui.lew4w1, self.ui.lew4w2, self.ui.lew4w3, self.ui.labelWort4Index, self.ui.labelWort4)
        self.__calulate(self.ui.lew5w1, self.ui.lew5w2, self.ui.lew5w3, self.ui.labelWort5Index, self.ui.labelWort5)
        self.__calulate(self.ui.lew6w1, self.ui.lew6w2, self.ui.lew6w3, self.ui.labelWort6Index, self.ui.labelWort6)
        self.__calulate(self.ui.lew7w1, self.ui.lew7w2, self.ui.lew7w3, self.ui.labelWort7Index, self.ui.labelWort7)
        self.__calulate(self.ui.lew8w1, self.ui.lew8w2, self.ui.lew8w3, self.ui.labelWort8Index, self.ui.labelWort8)
        self.__calulate(self.ui.lew9w1, self.ui.lew9w2, self.ui.lew9w3, self.ui.labelWort9Index, self.ui.labelWort9)
        self.__calulate(self.ui.lew10w1, self.ui.lew10w2, self.ui.lew10w3, self.ui.labelWort10Index, self.ui.labelWort10)
        self.__calulate(self.ui.lew11w1, self.ui.lew11w2, self.ui.lew11w3, self.ui.labelWort11Index, self.ui.labelWort11)
        self.__calulate(self.ui.lew12w1, self.ui.lew12w2, self.ui.lew12w3, self.ui.labelWort12Index, self.ui.labelWort12)
        self.__calulate(self.ui.lew13w1, self.ui.lew13w2, self.ui.lew13w3, self.ui.labelWort13Index, self.ui.labelWort13)
        self.__calulate(self.ui.lew14w1, self.ui.lew14w2, self.ui.lew14w3, self.ui.labelWort14Index, self.ui.labelWort14)
        self.__calulate(self.ui.lew15w1, self.ui.lew15w2, self.ui.lew15w3, self.ui.labelWort15Index, self.ui.labelWort15)
        self.__calulate(self.ui.lew16w1, self.ui.lew16w2, self.ui.lew16w3, self.ui.labelWort16Index, self.ui.labelWort16)
        self.__calulate(self.ui.lew17w1, self.ui.lew17w2, self.ui.lew17w3, self.ui.labelWort17Index, self.ui.labelWort17)
        self.__calulate(self.ui.lew18w1, self.ui.lew18w2, self.ui.lew18w3, self.ui.labelWort18Index, self.ui.labelWort18)
        self.__calulate(self.ui.lew19w1, self.ui.lew19w2, self.ui.lew19w3, self.ui.labelWort19Index, self.ui.labelWort19)
        self.__calulate(self.ui.lew20w1, self.ui.lew20w2, self.ui.lew20w3, self.ui.labelWort20Index, self.ui.labelWort20)
        self.__calulate(self.ui.lew21w1, self.ui.lew21w2, self.ui.lew21w3, self.ui.labelWort21Index, self.ui.labelWort21)
        self.__calulate(self.ui.lew22w1, self.ui.lew22w2, self.ui.lew22w3, self.ui.labelWort22Index, self.ui.labelWort22)
        self.__calulate(self.ui.lew23w1, self.ui.lew23w2, self.ui.lew23w3, self.ui.labelWort23Index, self.ui.labelWort23)

        if len(self.indexList) == 23:
            try:
                index = self.createHash()
                word = self.wortliste[index]
                self.ui.labelWort24.setText(word)
                self.ui.labelWort24Index.setText(str(index))
                self.seed += word
                self.ui.textEditSeed.setText(self.seed)

            except:
                self.seed = ''
                self.ui.labelWort24.setText('')
                self.ui.textEditSeed.setText('')
                self.ui.labelWort24Index.setText('')
        else:
            self.seed = ''
            self.ui.labelWort24.setText('')
            self.ui.textEditSeed.setText('')
            self.ui.labelWort24Index.setText('')
        return

        self.w24Liste = self.__find_word24_all()
        l = len(self.b)
        b2 = self.b

        print ("Laenge", l,b2)

        if len(self.w24Liste) == 8:
            try:
                wuerfel24 = int(self.ui.lew24w1.text())
                index = self.w24Liste[(wuerfel24-1) // 2]
                word = self.wortliste[index]
                self.ui.labelWort24.setText(word)
                self.ui.labelWort24Index.setText(str(index))
                self.seed += word
            except:
                self.seed = ''
                self.ui.labelWort24.setText('')

        else:
            self.seed = ''

        self.ui.textEditSeed.setText(self.seed)


    def buttonCalculate2(self):
        z1 = int(self.ui.lew1w1.text())
        z2 = int(self.ui.lew1w2.text())
        z3 = int(self.ui.lew1w3.text())
        index = self.getIndex(z1, z2, z3)
        self.ui.labelWort1Index.setText(str(index))
        self.ui.labelWort1.setText(self.wortliste[index])

    def readWortList(self):
        f = open('data/english.txt')

        # list = f.readlines()
        self.wortliste = f.read().splitlines()

        f.close()
        print (self.wortliste)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    W = TMainWindow()
    W.show()
    sys. exit(app. exec_())
