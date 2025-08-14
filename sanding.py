import random
def shuffle_block(input_path, output_path, start_line, block_length):
    """
    Shuffle ngẫu nhiên thứ tự các dòng trong một đoạn liên tiếp của file
    """
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    end_line = start_line + block_length
    block = lines[start_line:end_line]
    random.shuffle(block)
    lines[start_line:end_line] = block

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

shuffle_block("outputs/test_outputs.txt", "outputs/test_outputs.txt", 1000, 1500)