class Block:
    P_1000 = "█"    # 1.000%
    P_0875 = "▉"    # 0.875%
    P_0750 = "▊"    # 0.750%
    P_0625 = "▋"    # 0.625%
    P_0500 = "▌"    # 0.500% 
    P_0375 = "▍"    # 0.375%
    P_0250 = "▎"    # 0.250%
    P_0125 = "▏"    # 0.125%
    P_0000 = ""     # 0.000%


def get_decimal_block(decimal : float) -> str:        
    # TODO: fix floats compare
    if decimal < 0 or decimal > 1:
        return "X"

    if 0 <= decimal < 0.0625:
        return Block.P_0000
    if 0.0625 <= decimal < 0.1875:
        return Block.P_0125
    if 0.1875 <= decimal < 0.3125:
        return Block.P_0250
    if 0.3125 <= decimal < 0.4375:
        return Block.P_0375
    if 0.4375 <= decimal < 0.5625:
        return Block.P_0500
    if 0.5625 <= decimal < 0.6875:
        return Block.P_0625
    if 0.6875 <= decimal < 0.8125:
        return Block.P_0750
    if 0.8125 <= decimal < 0.9375:
        return Block.P_0875
    if 0.9375 <= decimal <= 1:
        return Block.P_1000


def get_bar(percentage : float):    
    decimals = 3        
    percentage_per_block = 10
    p_int = int(percentage * 10**decimals )    
    # get quantity of full blocks (10%)
    full_blocks = p_int // (10**decimals * percentage_per_block)
    bar = Block.P_1000 * full_blocks
    partial_block = p_int % (10**decimals * percentage_per_block)
    partial_block = partial_block / (10**decimals * percentage_per_block)
    bar += get_decimal_block(partial_block)
    bar += (" " * int(100/percentage_per_block - len(bar)))    
    return bar