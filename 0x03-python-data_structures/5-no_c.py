#!/usr/bin/env python3

def no_c(my_string):
    new_st = my_string.translate({ord('c'): None})
    new_st = new_st.translate({ord('C'): None})
    return new_st
