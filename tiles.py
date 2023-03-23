class UserTilePOS:
    def __init__(self, goal_x, goal_y, y, ):
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.y = y

    def call(self, scaler):
        if (self.y - self.goal_y) >= scaler:
            self.y = self.goal_y + (self.y - self.goal_y) / 2
        else:
            self.y = self.goal_y

    def push(self, scaler):
        if self.y >= (self.goal_y + 100 * scaler):
            self.y = (self.goal_y + 100 * scaler)
        elif self.y == self.goal_y:
            self.y += scaler
        else:
            self.y = self.goal_y + (self.y - self.goal_y)*2


def initial_tile_POS(scaler):
    user_tile_POS = [
        # Crop tile 1
        UserTilePOS(
            36 * scaler,
            7 * scaler,
            107 * scaler
        ),
        # Crop tile 2
        UserTilePOS(
            50 * scaler,
            14 * scaler,
            114 * scaler
        ),
        # Crop tile 3
        UserTilePOS(
            64 * scaler,
            21 * scaler,
            121 * scaler
        ),
        # Crop tile 4
        UserTilePOS(
            22 * scaler,
            14 * scaler,
            114 * scaler
        ),
        # Crop tile 5
        UserTilePOS(
            36 * scaler,
            21 * scaler,
            121 * scaler
        ),
        # Crop tile 6
        UserTilePOS(
            50 * scaler,
            28 * scaler,
            128 * scaler
        ),
        # Crop tile 7
        UserTilePOS(
            8 * scaler,
            21 * scaler,
            121 * scaler
        ),
        # Crop tile 8
        UserTilePOS(
            22 * scaler,
            28 * scaler,
            128 * scaler
        ),
        # Crop tile 9
        UserTilePOS(
            36 * scaler,
            35 * scaler,
            135 * scaler
        )
    ]
    return user_tile_POS
