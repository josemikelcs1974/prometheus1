/**
 * ⚡ PROMETHEUS — ETF Rotation Intelligence System
 * Dashboard React — FASE 1 COMPLETADA
 */

import React, { useState, useEffect } from 'react';
import { 
  Zap, 
  RefreshCcw, 
  Terminal, 
  ChevronRight,
  Activity,
  Cpu,
  ShieldCheck,
  AlertTriangle
} from 'lucide-react';
import { motion } from 'motion/react';
import { 
  SYSTEM_NAME, 
  SYSTEM_SUBTITLE, 
  SYSTEM_VERSION, 
  DEFAULT_REFRESH 
} from './config';
import AegisMonitor from './components/AegisMonitor';

const App: React.FC = () => {
  const [systemStatus] = useState("OK");
  const [lastUpdate, setLastUpdate] = useState(new Date());
  const [uptime, setUptime] = useState(0);
  const [hasIA] = useState(false);
  const [refreshInterval] = useState(DEFAULT_REFRESH);

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
    { num: "01", icon: "📊", name: "MACRO DASHBOARD", desc: "25 activos macro en tiempo real" },
    { num: "02", icon: "🔄", name: "ROTACIÓN SECTORIAL", desc: "Ranking 13 sectores + top-5 ETFs" },
    { num: "03", icon: "⚡", name: "AGENTE CRONOS", desc: "Analista macro IA (Claude)" },
    { num: "04", icon: "⚠️", name: "AGENTE NEMESIS", desc: "CRO / Abogado del Diablo" },
    { num: "05", icon: "🛡️", name: "MONITOR SISTEMA", desc: "AEGIS + logs en tiempo real" },
  ];

  return (
    <div className="flex h-screen bg-[#050508] text-[#e8e8f0] font-mono overflow-hidden select-none">
      <aside className="w-72 bg-[#08080f] border-r border-[#1a1a2e] flex flex-col p-5">
        <div className="mb-8">
          <div className="text-[#00ff88] font-bold text-xl tracking-[0.15em] py-2 border-b border-[#1a1a2e] flex items-center gap-2">
            <Zap size={20} fill="#00ff88" strokeWidth={0} />
            {SYSTEM_NAME}
          </div>
          <div className="text-[0.65rem] text-[#8888aa] tracking-[0.1em] uppercase mt-1">
            {SYSTEM_SUBTITLE}
          </div>
        </div>

        <div className="bg-[#0d0d14] border border-[#1a1a2e] rounded p-4 mb-6 shadow-inner">
          <div className="text-[0.68rem] text-[#8888aa] uppercase mb-2 flex justify-between items-center">
            <span>Estado del Sistema</span>
            <Activity size={10} className="animate-pulse" />
          </div>
          <div className="flex items-center gap-3 font-bold">
            <span className="text-[#00ff88] text-lg">🟢</span>
            <span className="text-[#00ff88] text-lg tracking-wider">{systemStatus}</span>
          </div>
        </div>

        <div className="mb-8">
          {hasIA ? (
            <div className="text-[#00ff88] text-[0.75rem] flex items-center gap-2 bg-[#00ff8811] p-2 border border-[#00ff8833] rounded">
              <ShieldCheck size={14} /> ✓ AGENTES IA ACTIVOS
            </div>
          ) : (
            <div className="text-[#ffaa00] text-[0.75rem] flex items-center gap-2 bg-[#ffaa0011] p-2 border border-[#ffaa0033] rounded">
              <AlertTriangle size={14} /> ⚠ SIN API KEY IA
            </div>
          )}
        </div>

        <nav className="space-y-6 flex-1 pr-1 overflow-y-auto custom-scrollbar">
           <div className="space-y-2">
              <div className="text-[#8888aa] text-[0.72rem] uppercase tracking-widest pl-1">Configuración</div>
              <div className="bg-[#0d0d14] border border-[#1a1a2e] rounded p-2.5 text-xs flex justify-between items-center cursor-pointer hover:bg-[#12121c] transition-colors group">
                <span className="group-hover:text-white uppercase">Refresh: {refreshInterval}</span>
                <span className="text-[0.6rem] opacity-50">▼</span>
              </div>
           </div>

           <div className="text-[0.7rem] text-[#444466] border-l-2 border-[#1a1a2e] pl-3 mt-4">
              Última actualización:<br />
              <span className="text-[#8888aa] font-bold">{lastUpdate.toLocaleTimeString()} UTC</span>
           </div>

           <button 
             onClick={() => { setLastUpdate(new Date()); }}
             className="w-full border border-[#00ff88] text-[#00ff88] p-3 text-xs rounded hover:bg-[#00ff88] hover:text-[#050508] transition-all flex items-center justify-center gap-2 font-bold uppercase tracking-[0.1em] shadow-[0_0_15px_rgba(0,255,136,0.05)] active:scale-[0.98]"
            >
              <RefreshCcw size={14} /> 
              Update Global
           </button>
        </nav>

        <div className="pt-6 border-t border-[#1a1a2e] text-[0.68rem] text-[#444466] text-center space-y-1">
          <div className="flex justify-center gap-2 items-center">
            <Cpu size={10} />
            <span>v{SYSTEM_VERSION} · UPTIME: {formatUptime(uptime)}</span>
          </div>
          <div className="text-[0.62rem] opacity-50 uppercase">Estado: Operativo</div>
        </div>
      </aside>

      <main className="flex-1 overflow-y-auto bg-[#050508] relative">
        <div className="absolute inset-x-0 top-0 h-96 bg-gradient-to-b from-[#00ff8808] to-transparent pointer-events-none" />
        
        <div className="max-w-5xl mx-auto px-8 py-12 flex flex-col min-h-full">
          <motion.div 
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center mb-16"
          >
            <h1 className="text-[#00ff88] font-bold text-6xl tracking-[0.12em] mb-4 drop-shadow-[0_0_25px_rgba(0,255,136,0.25)]">
              ⚡ {SYSTEM_NAME}
            </h1>
            <div className="flex items-center justify-center gap-6">
              <div className="h-[1px] w-16 bg-[#1a1a2e]" />
              <p className="text-[#8888aa] tracking-[0.5em] uppercase text-[0.65rem] font-black opacity-80">
                {SYSTEM_SUBTITLE}
              </p>
              <div className="h-[1px] w-16 bg-[#1a1a2e]" />
            </div>
          </motion.div>

          <div className="bg-[#0f0f18] border border-[#1a1a2e] rounded-lg p-10 shadow-[0_30px_60px_rgba(0,0,0,0.6)] backdrop-blur-md relative overflow-hidden group">
            <div className="absolute top-0 left-0 w-full h-[2px] bg-gradient-to-r from-transparent via-[#00ff88] to-transparent opacity-40" />
            
            <div className="text-[#8888aa] text-[0.72rem] tracking-[0.25em] uppercase mb-10 border-b border-[#1a1a2e] pb-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <Terminal size={14} className="text-[#00ff88]" /> 
                <span className="font-bold border-l-2 border-[#00ff88] pl-3 ml-1">Módulos de Sistema Fase 1</span>
              </div>
              <div className="text-[0.6rem] text-[#444466]">ACCESO INSTITUCIONAL / {new Date().getFullYear()}</div>
            </div>

            <div className="grid gap-3">
              {modules.map((m, i) => (
                <motion.div 
                  key={i}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.3 + i * 0.1 }}
                  className="flex items-center gap-6 p-5 border border-transparent rounded-md hover:border-[#1a1a2e] hover:bg-[#12121c] group transition-all cursor-pointer relative"
                >
                  <div className="absolute left-0 w-0.5 h-0 bg-[#00ff88] group-hover:h-8 transition-all duration-300" />
                  <div className="text-[#00ff88] text-[0.65rem] font-bold font-mono tracking-tighter opacity-30 group-hover:opacity-100 w-6">
                    {m.num}
                  </div>
                  <div className="text-[#00ff88] p-2.5 bg-[#00ff8808] border border-transparent group-hover:border-[#00ff8833] rounded-sm group-hover:bg-[#00ff88] group-hover:text-[#050508] transition-all duration-300 transform group-hover:rotate-12">
                    <span className="text-xl">{m.icon}</span>
                  </div>
                  <div className="flex flex-col">
                    <div className="text-[1rem] font-bold tracking-wider group-hover:text-white transition-colors uppercase">{m.name}</div>
                    <div className="text-[#8888aa] text-[0.75rem] tracking-tight group-hover:text-[#e8e8f0]/80 transition-colors italic">{m.desc}</div>
                  </div>
                  <div className="ml-auto opacity-0 group-hover:opacity-100 transition-all transform translate-x-4 group-hover:translate-x-0">
                    <ChevronRight size={18} className="text-[#00ff88]" />
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          <div className="mt-10">
            <AegisMonitor />
          </div>

          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.8 }}
            className="mt-12 text-[#444466] text-[0.65rem] text-center flex flex-col items-center gap-4"
          >
            <div className="flex items-center gap-3 animate-pulse opacity-50">
              <div className="h-[1px] w-8 bg-[#444466]" />
              <span className="tracking-[0.3em] font-bold uppercase">Ready for instruction</span>
              <div className="h-[1px] w-8 bg-[#444466]" />
            </div>
            
            {!hasIA && (
              <div className="max-w-md bg-[#ffaa0005] border border-[#ffaa0022] p-5 rounded text-[#ffaa00cc] leading-relaxed text-xs shadow-lg">
                <span className="font-bold border-b border-[#ffaa0044] pb-1 inline-block mb-2 uppercase tracking-widest text-[0.6rem]">⚠️ System Warning</span><br />
                <strong>Modo de Simulación Activo:</strong> Los agentes IA requieren configuración de API Key. 
                Los rankings técnicos y el motor de macro-análisis operan en modo analítico estático.
              </div>
            )}
          </motion.div>

          <footer className="mt-auto pt-20 pb-8 w-full">
            <div className="h-[1px] bg-gradient-to-r from-transparent via-[#1a1a2e] to-transparent mb-8" />
            <div className="flex flex-col gap-6 text-center">
              <div className="flex justify-center gap-8 text-[0.6rem] text-[#444466] tracking-[0.3em] uppercase font-black">
                <span className="hover:text-[#00ff88] transition-colors cursor-help">Yahoo Finance Data</span>
                <span className="opacity-20">•</span>
                <span className="hover:text-[#00ff88] transition-colors cursor-help">Claude 3.5 Sonnet IA</span>
                <span className="opacity-20">•</span>
                <span className="hover:text-[#00ff88] transition-colors cursor-help">TypeScript v5.x</span>
              </div>
              <div className="text-[0.6rem] text-[#222233] uppercase tracking-[0.1em] italic leading-loose max-w-2xl mx-auto opacity-70">
                PROMETHEUS v2.0.0 — Este sistema está diseñado para el análisis técnico institucional de rotación de ETFs. 
                El uso indebido de las señales generadas es responsabilidad del operador. 
                No constituye asesoramiento financiero formal.
              </div>
            </div>
          </footer>
        </div>
      </main>
      
      <style>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 2px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: #1a1a2e;
          border-radius: 10px;
        }
      `}</style>
    </div>
  );
};

export default App;
