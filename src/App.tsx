/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

/**
 * ⚡ PROMETHEUS — ETF Rotation Intelligence System
 * Dashboard React (Compatibilidad Replicada de Fase 1)
 */

import React, { useState, useEffect } from 'react';
import { 
  Zap, 
  BarChart3, 
  RefreshCcw, 
  AlertTriangle, 
  ShieldCheck, 
  ChevronRight,
  Activity,
  User,
  LayoutDashboard,
  Terminal,
  Settings
} from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';

const COLORS = {
  green: "#00ff88",
  red: "#ff3366",
  orange: "#ffaa00",
  text_primary: "#e8e8f0",
  text_secondary: "#8888aa",
  bg_sidebar: "#08080f",
  border: "#1a1a2e"
};

export default function App() {
  const [systemStatus, setSystemStatus] = useState("OK");
  const [lastUpdate, setLastUpdate] = useState(new Date());
  const [uptime, setUptime] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setUptime(prev => prev + 1);
      setLastUpdate(new Date());
    }, 60000); // Update every minute for demo
    return () => clearInterval(timer);
  }, []);

  const formatUptime = (seconds: number) => {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600));
    return `${h.toString().padStart(2, '0')}h ${m.toString().padStart(2, '0')}m`;
  };

  const modules = [
    { num: "01", icon: <BarChart3 size={18} />, name: "MACRO DASHBOARD", desc: "25 activos macro en tiempo real" },
    { num: "02", icon: <RefreshCcw size={18} />, name: "ROTACIÓN SECTORIAL", desc: "Ranking 13 sectores + top-5 ETFs" },
    { num: "03", icon: <Zap size={18} />, name: "AGENTE CRONOS", desc: "Analista macro IA (Claude)" },
    { num: "04", icon: <AlertTriangle size={18} />, name: "AGENTE NEMESIS", desc: "CRO / Abogado del Diablo" },
    { num: "05", icon: <ShieldCheck size={18} />, name: "MONITOR SISTEMA", desc: "AEGIS + logs en tiempo real" },
  ];

  return (
    <div className="flex h-screen bg-bg-main text-[#e8e8f0] font-mono overflow-hidden select-none">
      {/* Sidebar */}
      <aside className="w-64 bg-[#08080f] border-r border-border-dim flex flex-col p-4">
        <div className="mb-8">
          <div className="text-green-neon font-bold text-xl tracking-[0.15em] py-2 border-b border-border-dim flex items-center gap-2">
            <Zap size={20} fill="currentColor" />
            PROMETHEUS
          </div>
          <div className="text-[0.68rem] text-[#8888aa] tracking-[0.1em] uppercase mt-1">
            ETF Rotation Intelligence System
          </div>
        </div>

        {/* System Status Card */}
        <div className="bg-bg-secondary border border-border-dim rounded p-3 mb-4">
          <div className="text-[0.68rem] text-[#8888aa] uppercase mb-1">Estado del Sistema</div>
          <div className="flex items-center gap-2 font-bold">
            <span className="text-green-neon text-lg">🟢</span>
            <span className="text-green-neon">{systemStatus}</span>
          </div>
        </div>

        <div className="mb-4">
          <div className="text-green-neon text-[0.75rem] flex items-center gap-1">
            ✓ Agentes IA activos
          </div>
        </div>

        <div className="space-y-4">
           <div>
              <div className="text-[#8888aa] text-[0.72rem] uppercase mb-1">Auto-refresh</div>
              <div className="bg-bg-secondary border border-border-dim rounded p-2 text-sm flex justify-between items-center cursor-pointer hover:bg-bg-tertiary transition-colors">
                1 min
                <div className="text-[0.6rem]">▼</div>
              </div>
           </div>

           <div className="text-[0.7rem] text-[#444466]">
              Última actualización:<br />
              <span className="text-[#8888aa]">hace 0s</span>
           </div>

           <button className="w-full border border-green-neon text-green-neon p-2 text-xs rounded hover:bg-green-neon hover:text-bg-main transition-all flex items-center justify-center gap-2 font-bold uppercase tracking-wider shadow-[0_0_10px_rgba(0,255,136,0.1)] active:scale-[0.98]">
              <Zap size={14} /> 
              ACTUALIZACIÓN GLOBAL
           </button>
        </div>

        <div className="mt-auto pt-4 border-t border-border-dim text-[0.68rem] text-[#444466] text-center space-y-1">
          <div>v2.0.0 · Uptime: {formatUptime(uptime)}</div>
          <div>Datos: Yahoo Finance · IA: Claude API</div>
          <div className="text-[0.62rem]">⚠ Solo fines educativos</div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto p-8 flex flex-col items-center">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center w-full max-w-4xl"
        >
          <div className="mb-12">
            <h1 className="text-green-neon font-bold text-5xl tracking-[0.1em] mb-2 leading-tight">
              ⚡ PROMETHEUS
            </h1>
            <p className="text-[#8888aa] tracking-[0.25em] uppercase text-sm">
              ETF ROTATION INTELLIGENCE SYSTEM · v2.0.0
            </p>
          </div>

          <div className="bg-bg-secondary border border-border-dim rounded-lg p-8 text-left shadow-2xl">
            <div className="text-[#8888aa] text-[0.72rem] tracking-[0.12em] uppercase mb-6 border-b border-border-dim pb-2 flex items-center gap-2">
              <Terminal size={14} /> // MÓDULOS DISPONIBLES
            </div>

            <div className="space-y-2">
              {modules.map((m, i) => (
                <motion.div 
                  key={i}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.2 + i * 0.1 }}
                  className="flex items-center gap-4 py-3 border-b border-[#050508] last:border-0 hover:bg-[#12121c] px-2 rounded group transition-colors cursor-pointer"
                >
                  <span className="text-green-neon text-xs font-bold w-6">{m.num}</span>
                  <div className="text-green-neon group-hover:scale-110 transition-transform">{m.icon}</div>
                  <div className="text-[0.82rem] font-bold group-hover:text-white transition-colors">{m.name}</div>
                  <div className="text-[#8888aa] text-[0.75rem] ml-auto opacity-70 group-hover:opacity-100 transition-opacity">
                    — {m.desc}
                  </div>
                  <ChevronRight size={14} className="text-[#444466] group-hover:text-green-neon ml-2" />
                </motion.div>
              ))}
            </div>
          </div>

          <div className="mt-8 text-[#8888aa] text-sm italic">
            Navega usando el menú lateral izquierdo ←
          </div>

          <div className="prometheus-divider" />

          <footer className="text-center text-[0.68rem] text-[#444466] pb-8">
            <div className="flex justify-center gap-4 mb-2">
              <span>⚡ PROMETHEUS 2.0.0</span>
              <span>•</span>
              <span>Datos: Yahoo Finance</span>
              <span>•</span>
              <span>IA: Claude API</span>
              <span>•</span>
              <span>{lastUpdate.toISOString().replace('T', ' ').substring(0, 19)} UTC</span>
            </div>
            <div className="text-[0.60rem] opacity-60">
              ⚠️ Solo fines educativos. No constituye asesoramiento financiero.
            </div>
          </footer>
        </motion.div>
      </main>
    </div>
  );
}
