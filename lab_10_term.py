import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Значение средней приведённой температуры
T_plus = 309.84 / 289.7
n_continuous = np.linspace(0.05, 2.5, 500)

# Рассчёт значений для Ван дер Ваальса
A = 1 / (1 - n_continuous / 3)
B = (9 / 4) * (n_continuous / A)
C = (9 / 8) * n_continuous
D = B / A
Z = A - C / T_plus

alpha_P_vdv = 1 / (A - B / T_plus)
c_V_vdv = 3/2 * np.ones(len(n_continuous))
c_P_vdv = c_V_vdv +alpha_P_vdv * A
b_T_vdv = Z / (A ** 2) / (1 - D / T_plus)
b_s_vdv = b_T_vdv * c_V_vdv / c_P_vdv
a = 1 / np.sqrt(b_s_vdv)

# Импорт таблицы (пропуски обозначены '-')
df = pd.read_csv('exp.csv', na_values='-')

# График коэффициента термического расширения
fig, ax = plt.subplots(1,1)

ax.plot(df['n+'], df['ap+'], color='blue', linestyle='', marker='s', linewidth=2, label=r'Эксперимент')
ax.plot(n_continuous, alpha_P_vdv, color='blue', linestyle='--', linewidth=2, label=r'Ван дер Ваальс')
ax.plot(n_continuous, np.ones(len(n_continuous)), color='gray', alpha=0.5, linestyle='-', linewidth=2, label=r'Идеальный газ')

ax.set_title('Коэффициент термического расширения', fontsize=14)
ax.set_xlabel(r'$n^+$', fontsize=12)
ax.set_ylabel(r'$\alpha^+_p$', fontsize=12)
ax.grid(True)
ax.legend()

# График теплоёмкостей
fig1, ax1 = plt.subplots(1,1)

ax1.plot(df['n+'], df['cp+'], color='red', linestyle='', marker='s', linewidth=2, label=r'$c_p^+$ (Эксперимент)')
ax1.plot(n_continuous, c_P_vdv, color='red', linestyle='--', linewidth=2, label=r'$c_p^+$ Ван дер Ваальс')
ax1.plot(n_continuous, 2.5 * np.ones(len(n_continuous)), color='black', alpha=0.5, linestyle='-', linewidth=2, label=r'$c_p^+$ Идеальный газ')

ax1.plot(df['n+'], df['cV+'], color='blue', linestyle='', marker='s', linewidth=2, label=r'$c_v^+$ (Эксперимент)')
ax1.plot(n_continuous, c_V_vdv, color='blue', linestyle='--', linewidth=2, label=r'$c_v^+$ Ван дер Ваальс')
ax1.plot(n_continuous, 1.5 * np.ones(len(n_continuous)), color='gray', alpha=0.5, linestyle='-', linewidth=2, label=r'$c_v^+$ Идеальный газ')

ax1.set_title(r'Теплоёмкости $c_p^+$ и $c_V^+$', fontsize=14)
ax1.set_xlabel(r'$n^+$', fontsize=12)
ax1.set_ylabel(r'$c^+$', fontsize=12)
ax1.grid(True)
ax1.legend()

# График коэффициентов сжимаемости
fig2, ax2 = plt.subplots(1,1)

ax2.plot(df['n+'], df['T+'], color='red', linestyle='', marker='s', linewidth=2, label=r'$\beta_T^+$ (Эксперимент)')
ax2.plot(n_continuous, b_T_vdv, color='red', linestyle='--', linewidth=2, label=r'$\beta_T^+$ Ван дер Ваальс')
ax2.plot(n_continuous, np.ones(len(n_continuous)), color='black', alpha=0.5, linestyle='-', linewidth=2, label=r'$\beta_T^+$ Идеальный газ')

ax2.plot(df['n+'], df['s+'], color='blue', linestyle='', marker='s', linewidth=2, label=r'$\beta_s^+$ (Эксперимент)')
ax2.plot(n_continuous, b_s_vdv, color='blue', linestyle='--', linewidth=2, label=r'$\beta_s^+$ Ван дер Ваальс')
ax2.plot(n_continuous, 0.6 * np.ones(len(n_continuous)), color='gray', alpha=0.5, linestyle='-', linewidth=2, label=r'$\beta_s^+$ Идеальный газ')

ax2.set_title(r'Коэффициенты сжимаемости $\beta_T^+$ и $\beta_s^+$', fontsize=14)
ax2.set_xlabel(r'$n^+$', fontsize=12)
ax2.set_ylabel(r'$\beta^+$', fontsize=12)
ax2.grid(True)
ax2.legend()

# График скорости звука и сжимаемости
fig3, ax3 = plt.subplots(1,1)

ax3.plot(df['n+'], df['a+'], color='red', linestyle='', marker='s', linewidth=2, label=r'$a^+$ (Эксперимент)')
ax3.plot(n_continuous, a, color='red', linestyle='--', linewidth=2, label=r'$a^+$ Ван дер Ваальс')
ax3.plot(n_continuous, np.sqrt(5 / 3) * np.ones(len(n_continuous)), color='black', alpha=0.5, linestyle='-', linewidth=2, label=r'$a^+$ Идеальный газ')

ax3.plot(df['n+'], df['Z'], color='blue', linestyle='', marker='s', linewidth=2, label=r'$Z$ (Эксперимент)')
ax3.plot(n_continuous, Z * np.ones(len(n_continuous)), color='blue', linestyle='--', linewidth=2, label=r'$Z$ Ван дер Ваальс')
ax3.plot(n_continuous, np.ones(len(n_continuous)), color='gray', alpha=0.5, linestyle='-', linewidth=2, label=r'$Z$ Идеальный газ')

ax3.set_title(r'Скорость звука $a^+$ и коэффициент сжимаемости $Z$', fontsize=14)
ax3.set_xlabel(r'$n^+$', fontsize=12)
ax3.set_ylabel(r'', fontsize=12)
ax3.grid(True)
ax3.legend()

plt.show()

