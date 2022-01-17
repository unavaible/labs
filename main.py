from subject_area.detail import Detail
from subject_area.manufacturer import Manufacturer
from subject_area.details_man import DetailsMan

from operator import itemgetter

manufacturers = [
    Manufacturer(1, "Russian Manufacturer", "Russia"),
    Manufacturer(2, "English Manufacturer", "UK"),
    Manufacturer(3, "Chad Manufacturer", "Chad"),
]

details = [
    Detail(1, "wire", "copper", 1),
    Detail(2, "washer", "lead", 2),
    Detail(3, "screw", "aluminum", 3),
    Detail(4, "bullet", "gold", 3)
]


details_man = [
    DetailsMan(1, 1),
    DetailsMan(1, 2),

    DetailsMan(2, 2),
    DetailsMan(2, 3),

    DetailsMan(3, 3),
    DetailsMan(3, 1),

    DetailsMan(4, 3),
    DetailsMan(4, 2)
]

def main():

    one_to_many = [(det.name, man.name, man.country)
                   for det in details
                   for man in manufacturers
                   if det.man_id == man.id
                   ]

    many_to_many_temp = [(man.name, dp.man_id, dp.detail_id)
                         for man in manufacturers
                         for dp in details_man
                         if man.id == dp.man_id]

    many_to_many = [(det.name, man_name)
                    for man_name, man_id, detail_id in many_to_many_temp
                    for det in details if det.id == detail_id]

    print('\nЗадание Б1')
    task_1 = sorted(one_to_many, key=itemgetter(0))
    print(task_1)


    print('\nЗадание Б2')
    task_2 = []
    for man in manufacturers:
        det_man = list(filter(lambda elem: elem[1] == man.name, one_to_many))
        task_2.append([man.name, len(det_man)])
    print(sorted(task_2, key=itemgetter(1)))


    print('\nЗадание Б3')
    task_3 = {}
    for det in details:
        if (det.name.startswith('b') or det.name.startswith('s')):
            det_man = list(
                filter(lambda elem: elem[0] == det.name, many_to_many))
            task_3[det.name] = [x for _, x in det_man]
    print(task_3)

if __name__ == "__main__":
    main()