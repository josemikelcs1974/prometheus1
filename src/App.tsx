/**
 * ⚡ PROMETHEUS — ETF Rotation Intelligence System
 * Dashboard React — FASE 1 COMPLETADA
 */

import React, { useState, useEffect } from 'react';
import { 
  Zap, 
  BarChart3, 
  RefreshCcw, 
  AlertTriangle, 
  ShieldCheck, 
  ChevronRight,
  Terminal,
  Activity,
  Cpu
} from 'lucide-react';
import { motion } from 'motion/react';

const COLORS = {
  green: "#00ff88",
  red: "#ff3366",
  orange: "#ffaa00",
  blue: "#00aaff",
  text_primary: "#e8e8f0",
  text_secondary: "#8888aa",
  bg_sidebar: "#08080f",
  border: "#1a1a2e"
};

export default function App() {
  const [systemStatus, setSystemStatus] = useState("OK");
  const [lastUpdate, setLastUpdate] = useState(new Date());
  const [uptime, setUptime] = useState(0);
  const [hasIA, setHasIA] = useState(false);

  useEffect(() => {
    const timer = setInterval(() => {
      setUptime(prev => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const formatUptime = (seconds: number) => {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = seconds % 60;
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
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
      {/* Sidebar - Bloomberg Inspired */}
      <aside className="w-72 bg-[#08080f] border-r border-border-dim flex flex-col p-5">
        <div className="mb-8">
          <div className="text-green-neon font-bold text-xl tracking-[0.15em] py-2 border-b border-border-dim flex items-center gap-2">
            <Zap size={20} fill="#00ff88" strokeWidth={0} />
            PROMETHEUS
          </div>
          <div className="text-[0.65rem] text-[#8888aa] tracking-[0.1em] uppercase mt-1">
            ETF Rotation Intelligence System
          </div>
        </div>

        {/* System Status Panel */}
        <div className="bg-bg-secondary border border-border-dim rounded p-4 mb-6 shadow-inner">
          <div className="text-[0.68rem] text-[#8888aa] uppercase mb-2 flex justify-between items-center">
            <span>Estado del Sistema</span>
            <Activity size={10} className="animate-pulse" />
          </div>
          <div className="flex items-center gap-3 font-bold">
            <span className="text-green-neon text-lg">🟢</span>
            <span className="text-green-neon text-lg tracking-wider">{systemStatus}</span>
          </div>
        </div>

        {/* IA Status Badge */}
        <div className="mb-8">
          {hasIA ? (
            <div className="text-green-neon text-[0.75rem] flex items-center gap-2 bg-[#00ff8811] p-2 border border-[#00ff8833] rounded">
              <ShieldCheck size={14} /> ✓ AGENTES IA ACTIVOS
            </div>
          ) : (
            <div className="text-orange-neon text-[0.75rem] flex items-center gap-2 bg-[#ffaa0011] p-2 border border-[#ffaa0033] rounded">
              <AlertTriangle size={14} /> ⚠ SIN API KEY IA
            </div>
          )}
        </div>

        <nav className="space-y-6 flex-1">
           <div className="space-y-2">
              <div className="text-[#8888aa] text-[0.72rem] uppercase tracking-widest pl-1">Configuración</div>
              <div className="bg-bg-secondary border border-border-dim rounded p-2.5 text-xs flex justify-between items-center cursor-pointer hover:bg-bg-tertiary transition-colors">
                <span>AUTO-REFRESH: 1 MIN</span>
                <span className="text-[0.6rem] opacity-50">▼</span>
              </div>
           </div>

           <div className="text-[0.7rem] text-[#444466] border-l-2 border-border-dim pl-3 mt-4">
              Última actualización:<br />
              <span className="text-[#8888aa] font-bold">{lastUpdate.toLocaleTimeString()} UTC</span>
           </div>

           <button 
             onClick={() => { setLastUpdate(new Date()); }}
             className="w-full border border-green-neon text-green-neon p-3 text-xs rounded hover:bg-green-neon hover:text-bg-main transition-all flex items-center justify-center gap-2 font-bold uppercase tracking-[0.1em] shadow-[0_0_15px_rgba(0,255,136,0.05)] active:scale-[0.98]"
            >
              <RefreshCcw size={14} /> 
              Actualización Global
           </button>
        </nav>

        <div className="pt-6 border-t border-border-dim text-[0.68rem] text-[#444466] text-center space-y-1">
          <div className="flex justify-center gap-2 items-center">
            <Cpu size={10} />
            <span>v2.0.0 · UPTIME: {formatUptime(uptime)}</span>
          </div>
          <div>ESTADO: OPERATIVO</div>
        </div>
      </aside>

      {/* Main Content Stage */}
      <main className="flex-1 overflow-y-auto bg-bg-main relative">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(0,255,136,0.03),transparent)] pointer-events-none" />
        
        <div className="max-w-5xl mx-auto px-8 py-12 flex flex-col min-h-full">
          <motion.div 
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center mb-16"
          >
            <h1 className="text-green-neon font-bold text-6xl tracking-[0.1em] mb-4 drop-shadow-[0_0_20px_rgba(0,255,136,0.2)]">
              ⚡ PROMETHEUS
            </h1>
            <div className="flex items-center justify-center gap-4">
              <div className="h-[1px] w-12 bg-border-dim" />
              <p className="text-[#8888aa] tracking-[0.4em] uppercase text-xs font-bold">
                ETF ROTATION INTELLIGENCE SYSTEM
              </p>
              <div className="h-[1px] w-12 bg-border-dim" />
            </div>
          </motion.div>

          <div className="bg-bg-secondary border border-border-dim rounded-lg p-10 shadow-[0_20px_50px_rgba(0,0,0,0.5)] backdrop-blur-sm relative overflow-hidden group">
            <div className="absolute top-0 left-0 w-full h-[2px] bg-gradient-to-right from-transparent via-green-neon to-transparent opacity-30" />
            
            <div className="text-[#8888aa] text-[0.75rem] tracking-[0.2em] uppercase mb-8 border-b border-border-dim pb-3 flex items-center gap-3">
              <Terminal size={14} className="text-green-neon" /> 
              <span>Módulos de Inteligencia Disponibles</span>
            </div>

            <div className="grid gap-3">
              {modules.map((m, i) => (
                <motion.div 
                  key={i}
                  initial={{ opacity: 0, x: -15 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.3 + i * 0.1 }}
                  className="flex items-center gap-5 p-4 border border-transparent rounded-md hover:border-border-dim hover:bg-bg-tertiary group transition-all cursor-pointer"
                >
                  <div className="text-green-neon text-xs font-bold font-mono tracking-tighter opacity-50 group-hover:opacity-100">{m.num}</div>
                  <div className="text-green-neon p-2 bg-[#00ff8808] rounded group-hover:bg-green-neon group-hover:text-bg-main transition-colors">{m.icon}</div>
                  <div className="flex flex-col">
                    <div className="text-[0.9rem] font-bold tracking-wide group-hover:text-white transition-colors">{m.name}</div>
                    <div className="text-[#8888aa] text-[0.72rem] tracking-tight">{m.desc}</div>
                  </div>
                  <div className="ml-auto opacity-0 group-hover:opacity-100 transition-opacity">
                    <ChevronRight size={16} className="text-green-neon" />
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.2 }}
            className="mt-10 text-[#444466] text-xs text-center flex flex-col items-center gap-4"
          >
            <span className="animate-bounce">Navega usando el menú lateral izquierdo ←</span>
            
            {!hasIA && (
              <div className="max-w-md bg-[#ffaa0008] border border-orange-neon/20 p-4 rounded text-orange-neon/80 leading-relaxed">
                ⚠️ <strong>Modo de Datos Activo:</strong> Los agentes IA requieren configuración de API Key. 
                Los rankings técnicos y el motor de macro-análisis operan en modo analítico estándar.
              </div>
            )}
          </motion.div>

          <footer className="mt-auto pt-16 pb-6 w-full">
            <div className="prometheus-divider" />
            <div className="flex flex-col gap-4 text-center">
              <div className="flex justify-center gap-6 text-[0.65rem] text-[#444466] tracking-widest uppercase font-bold">
                <span className="hover:text-green-neon transition-colors cursor-help">Yahoo Finance Data</span>
                <span>•</span>
                <span className="hover:text-green-neon transition-colors cursor-help">Claude 3.5 Intelligence</span>
                <span>•</span>
                <span className="hover:text-green-neon transition-colors cursor-help">Streamlit Core Native</span>
              </div>
              <div className="text-[0.6rem] text-[#333344] uppercase tracking-tighter italic">
                Aviso: Sistema institucional de uso educativo. No garantizamos beneficios financieros ni exactitud absoluta de señales.
              </div>
            </div>
          </footer>
        </div>
      </main>
    </div>
  );
}

