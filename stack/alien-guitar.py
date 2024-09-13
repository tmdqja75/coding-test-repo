def min_finger_movement(num_notes, num_fret, song):
    string_stacks = [list() for _ in range(num_notes)]
    movement = 0
    for (string, note) in song:
        print(string, note)
        if len(string_stacks[string-1])==0:
            string_stacks[string-1].append(note)
            movement += 1
            continue
        
        if string_stacks[string-1][-1] < note:
            string_stacks[string-1].append(note)
            movement += 1
        elif string_stacks[string-1][-1] > note:
            while string_stacks[string-1][-1] > note or len(string_stacks)!=0:
                print(string_stacks[string-1])
                string_stacks[string-1].pop()
                movement += 1
            string_stacks[string-1].append(note)
            movement += 1
        else:
            continue
    return movement

song = [(1, 5), 
 (2, 3), 
 (2, 5), 
 (2, 7), 
 (2, 4), 
 (1, 5), 
 (1, 3)]

print(min_finger_movement(7, 15, song))