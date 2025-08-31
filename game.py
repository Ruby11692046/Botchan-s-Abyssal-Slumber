import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Botchan Prototype")
        self.x = 72
        self.y = 100
        self.bullets = []
        self.enemies = [{"x": 80, "y": 40}]
        pyxel.run(self.update, self.draw)

    def update(self):
        # プレイヤー移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2

        # スペースキーで弾発射
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullets.append({"x": self.x + 3, "y": self.y})

        # 弾の更新
        for b in self.bullets:
            b["y"] -= 4
        self.bullets = [b for b in self.bullets if b["y"] > 0]

        # 当たり判定（超シンプル）
        for e in self.enemies:
            for b in self.bullets:
                if abs(e["x"] - b["x"]) < 4 and abs(e["y"] - b["y"]) < 4:
                    e["hit"] = True

        self.enemies = [e for e in self.enemies if not e.get("hit")]

    def draw(self):
        pyxel.cls(0)
        # プレイヤー（青四角）
        pyxel.rect(self.x, self.y, 8, 8, 11)
        # 弾（白）
        for b in self.bullets:
            pyxel.rect(b["x"], b["y"], 2, 2, 7)
        # 敵（赤四角）
        for e in self.enemies:
            pyxel.rect(e["x"], e["y"], 8, 8, 8)

App()
