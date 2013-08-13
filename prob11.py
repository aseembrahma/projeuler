fp = open("prob11grid.txt", "r")
rows = fp.read().split("\n")
contents = [x.split(" ") for x in rows]
num_rows = len(contents)
num_cols = len(contents[0])
contents = [map(int, x) for x in contents]
seq_length = 4
max_product = -1

for i in range(num_rows):
    for j in range(num_cols):
        if num_rows-i >= seq_length:
            max_product = max(max_product, contents[i][j]*contents[i+1][j]*contents[i+2][j]*contents[i+3][j])
        if num_cols-j >= seq_length:
            max_product = max(max_product, contents[i][j]*contents[i][j+1]*contents[i][j+2]*contents[i][j+3])
        if num_rows-i >= seq_length and num_cols-j >= seq_length:
            max_product = max(max_product, contents[i][j]*contents[i+1][j+1]*contents[i+2][j+2]*contents[i+3][j+3])
        if num_rows-i >= seq_length and j+1 >= seq_length:
            max_product = max(max_product, contents[i][j]*contents[i+1][j-1]*contents[i+2][j-2]*contents[i+3][j-3])
        """
        temp_product = -1
        if i >= seq_length - 1 and j < seq_length - 1:
            temp_product = reduce(lambda x, y: x*y, [contents[x][j] for x in range(i-4+1, i+1)])
        elif j >= seq_length - 1 and i < seq_length - 1:
            temp_product = reduce(lambda x, y: x*y, [contents[x][j] for x in range(i-4+1, i+1)])
        elif i >= seq_length - 1 and j >= seq_length - 1:
            temp_product = reduce(lambda x, y: x*y, [contents[x][j] for x in range(i-4+1, i+1)])
            
        max_product = max(max_product, temp_product)
        """
print max_product