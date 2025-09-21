# Deploying the Centering Materials Rental App on Render

This version includes a **Tailwind-based UI** and APIs.

## Steps

1. Push this folder to a new GitHub repo.

2. Go to [Render](https://render.com), connect your GitHub, click "New +" → "Web Service".

3. Render detects `render.yaml` and builds automatically.

4. After 2–3 minutes, you'll get a link like:
   ```
   https://centering-rental-app.onrender.com
   ```

5. Visit that link to use the app:
   - `/` → Web UI (browse materials, add to cart, checkout)
   - `/api/materials` → list materials
   - `/api/orders` → list orders
