"""Event keys enums"""

from enum import IntEnum

import pygame.constants as pg_keys


class Keys(IntEnum):
    """Enum containing all the keyboard keys"""

    A = pg_keys.K_a
    B = pg_keys.K_b
    C = pg_keys.K_c
    D = pg_keys.K_d
    E = pg_keys.K_e
    F = pg_keys.K_f
    G = pg_keys.K_g
    H = pg_keys.K_h
    I = pg_keys.K_i
    J = pg_keys.K_j
    K = pg_keys.K_k
    L = pg_keys.K_l
    M = pg_keys.K_m
    N = pg_keys.K_n
    O = pg_keys.K_o
    P = pg_keys.K_p
    Q = pg_keys.K_q
    R = pg_keys.K_r
    S = pg_keys.K_s
    T = pg_keys.K_t
    U = pg_keys.K_u
    V = pg_keys.K_v
    W = pg_keys.K_w
    X = pg_keys.K_x
    Y = pg_keys.K_y
    Z = pg_keys.K_z

    UP = pg_keys.K_UP
    DOWN = pg_keys.K_DOWN
    LEFT = pg_keys.K_LEFT
    RIGHT = pg_keys.K_RIGHT

    SPACE = pg_keys.K_SPACE
    ESCAPE = pg_keys.K_ESCAPE
    RETURN = pg_keys.K_RETURN

    LEFT_SHIFT = pg_keys.K_LSHIFT
    RIGHT_SHIFT = pg_keys.K_RSHIFT

    LEFT_CTRL = pg_keys.K_LCTRL
    RIGHT_CTRL = pg_keys.K_RCTRL

    LEFT_ALT = pg_keys.K_LALT
    RIGHT_ALT = pg_keys.K_RALT

    TAB = pg_keys.K_TAB

    F1 = pg_keys.K_F1
    F2 = pg_keys.K_F2
    F3 = pg_keys.K_F3
    F4 = pg_keys.K_F4
    F5 = pg_keys.K_F5
    F6 = pg_keys.K_F6
    F7 = pg_keys.K_F7
    F8 = pg_keys.K_F8
    F9 = pg_keys.K_F9
    F10 = pg_keys.K_F10
    F11 = pg_keys.K_F11
    F12 = pg_keys.K_F12


del pg_keys
