import json
import sys

JDATA = "ATtiny85.json"
class Decoder:
    
    def __init__(self, filename):
        try:
            fin = open(filename)
        except:
            print("Cannot open data file")
            sys.exit(1)
        self.jdata = json.load(fin)
    
    def dump(self):
        patterns = {}
        for j in self.jdata:
            # patterns are nested dictionaries keyed by nibble patterns
            bits = j["Bits"]
            nibs = bits.split()
            n1 = nibs[0]
            n2 = nibs[1]
            n3 = nibs[2]
            n4 = nibs[3]
            instruction = j["Mnemonic"]
            try:
                instruction += " " + j["Operands"]
            except:
                pass
            if not n1 in patterns:
                patterns[n1] = {}
            
            if not n2 in patterns[n1]:
                patterns[n1][n2] = {}
            if not n3 in patterns[n1][n2]:
                patterns[n1][n2][n3] = {}
            if not n4 in patterns[n1][n2][n3]:
                patterns[n1][n2][n3][n4] = {}
            patterns[n1][n2][n3][n4]["inst"] = instruction
            patterns[n1][n2][n3][n4]["bits"] = bits
        
        n1keys = sorted(patterns)
        print("\n\n")
        for m1 in n1keys:
            print(m1)
            level1 = patterns[m1]
            n2keys = sorted(level1)
            for m2 in n2keys:
                print ("\t",m2)
                level2 = level1[m2]
                n3keys = sorted(level2)
                for m3 in n3keys:
                    print("\t\t",m3)
                    level3 = level2[m3]
                    n4keys = sorted(level3)
                    for m4 in n4keys:
                        print("\t\t\t", m4, level3[m4])



if __name__ == "__main__":
    print("Sorting");
    jloader = Decoder(JDATA)
    jloader.dump()
