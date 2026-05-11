import express from "express";
import { createServer as createViteServer } from "vite";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function startServer() {
  const app = express();
  const PORT = 3000;

  // Middleware
  app.use(express.json());

  // API Routes - PROMETHEUS Core Interface
  app.get("/api/v1/health", (req, res) => {
    res.json({ 
      status: "online", 
      system: "PROMETHEUS", 
      version: "2.0.0",
      timestamp: new Date().toISOString()
    });
  });

  // Vite Integration
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.resolve(__dirname, "dist");
    app.use(express.static(distPath));
    app.get("*", (req, res) => {
      res.sendFile(path.join(distPath, "index.html"));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`
  ⚡ PROMETHEUS CORE ACTIVATED
  ----------------------------
  Terminal: http://0.0.0.0:${PORT}
  Ambiente: ${process.env.NODE_ENV || 'development'}
    `);
  });
}

startServer().catch(err => {
  console.error("CRITICAL SYSTEM FAILURE:", err);
  process.exit(1);
});
