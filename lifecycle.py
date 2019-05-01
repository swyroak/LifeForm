from checkingfield import Checkingfield
from createfield import Field
from juddingfield import juddingfield


def basecycle(basefield):
    formingfield = Checkingfield(basefield)
    formingfield.slicing_all()
    nextfield = juddingfield(formingfield.get_summaryslicedfields(), basefield)
    nextfield.judging_life()
    output = nextfield.get_futurefield()
    return output


if __name__ == "__main__":
    basefield = Field()
    cycles = []
    cycles.append(basecycle(basefield.get_room()))
    for i in range(11):
        cycles.append(basecycle(cycles[i]))

    for cycle in cycles:
        print(cycle)
