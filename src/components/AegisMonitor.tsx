import React, { useState, useEffect, useRef } from 'react';
import { Terminal } from 'lucide-react';

interface LogEntry {
  timestamp: string;
  message: string;
  type: 'info' | 'warn' | 'success' | 'error';
}

const AegisMonitor: React.FC = () => {
  const [logs, setLogs] = useState<LogEntry[]>([
    { timestamp: new Date().toISOString(), message: "PROMETHEUS Core Interface v2.0.0 Initialized", type: 'info' },
    { timestamp: new Date().toISOString(), message: "Loading ETF Sector Weights (13 Sectors)", type: 'info' },
  ]);
  
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const messages = [
      "Connecting to macro-data-provider: Yahoo Finance...",
      "Sincronizando con GitHub Repository (josemikel74/prometheus)...",
      "AEGIS Shield Protection Active [LEVEL 1]",
      "Scanning Technical Momentum for 130 ETFs...",
      "Waiting for global refresh command...",
      "INFO: System running in Simulation Mode (No API detected)",
      "Sector Rotation Matrix updated successfully",
      "Macro cycle detected: LATE EXPANSION / PEAK",
    ];

    const interval = setInterval(() => {
      const randomMsg = messages[Math.floor(Math.random() * messages.length)];
      setLogs(prev => [...prev.slice(-49), { 
        timestamp: new Date().toISOString(), 
        message: randomMsg,
        type: randomMsg.includes('INFO') ? 'warn' : (randomMsg.includes('successfully') ? 'success' : 'info')
      }]);
    }, 4000);

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [logs]);

  return (
    <div className="bg-[#08080c] border border-[#1a1a2e] rounded p-4 font-mono shadow-inner group">
      <div className="flex justify-between items-center mb-3">
        <div className="text-[#00ff88] text-[0.65rem] flex items-center gap-2">
          <div className="w-2 h-2 bg-[#00ff88] rounded-full animate-pulse" />
          AEGIS SYSTEM LOGS [LIVE]
        </div>
        <div className="text-[#444466] text-[0.6rem] group-hover:text-[#8888aa] transition-colors tracking-tighter">
          TERMINAL 01 / PROMETHEUS_CORE
        </div>
      </div>
      
      <div className="h-48 overflow-y-auto space-y-1.5 text-[0.68rem] leading-relaxed pr-2 custom-scrollbar scroll-smooth">
        {logs.map((log, i) => (
          <div key={i} className="flex gap-3">
            <span className="text-[#444466] shrink-0 font-bold">[{log.timestamp.split('T')[1].split('.')[0]}]</span>
            <span className={`
              ${log.type === 'success' ? 'text-[#00ff88]' : ''}
              ${log.type === 'warn' ? 'text-[#ffaa00]' : ''}
              ${log.type === 'info' ? 'text-[#00ff88]/70' : ''}
              ${log.type === 'error' ? 'text-[#ff3366]' : ''}
             uppercase tracking-tight`}>
              {log.message}
            </span>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>
      
      <style>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 3px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: #050508;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: #1a1a2e;
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: #333344;
        }
      `}</style>
    </div>
  );
};

export default AegisMonitor;
