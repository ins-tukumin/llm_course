import matplotlib.pyplot as plt

# データの準備
conditions = ['C', 'R,R⁺']
understanding = [3.4, 4.3]  # R,R⁺の満足度がCより高い

# グラフの作成
fig, ax = plt.subplots()
ax.bar(conditions, understanding, color=['blue', 'green'])

# グラフのラベルとタイトル
ax.set_xlabel('Conditions')
ax.set_ylabel('understanding')
ax.set_title('Comparison of Satisfaction between C and R,R⁺')

# y軸の範囲を設定
ax.set_ylim(0, 5)

# 画像として保存
plt.savefig('satisfaction_comparison.png')

# 画像を表示
plt.show()
