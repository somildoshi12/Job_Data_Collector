import { useEffect, useState } from 'react'
import { createClient } from '@supabase/supabase-js'
import { motion } from 'framer-motion'
import { MapPin, Calendar, ExternalLink, Briefcase, Search } from 'lucide-react'
import './index.css'

// Initialize Supabase (We will use Env vars in production, but for now hardcode or use Vite env)
const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseKey = import.meta.env.VITE_SUPABASE_KEY
const supabase = createClient(supabaseUrl, supabaseKey)

function App() {
    const [jobs, setJobs] = useState([])
    const [filter, setFilter] = useState('')
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetchJobs()
    }, [])

    async function fetchJobs() {
        try {
            const { data, error } = await supabase
                .table('jobs')
                .select(`
          *,
          companies ( name )
        `)
                .order('posted_date', { ascending: false })

            if (error) throw error
            setJobs(data)
        } catch (error) {
            console.error('Error fetching jobs:', error)
        } finally {
            setLoading(false)
        }
    }

    const filteredJobs = jobs.filter(job =>
        job.title.toLowerCase().includes(filter.toLowerCase()) ||
        job.companies?.name.toLowerCase().includes(filter.toLowerCase())
    )

    return (
        <div className="min-h-screen p-8 text-white relative overflow-hidden">
            {/* Background Blobs for Glass Effect */}
            <div className="fixed top-0 left-0 w-96 h-96 bg-purple-600 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob"></div>
            <div className="fixed top-0 right-0 w-96 h-96 bg-blue-600 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-2000"></div>
            <div className="fixed -bottom-8 left-20 w-96 h-96 bg-pink-600 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-4000"></div>

            <div className="max-w-6xl mx-auto relative z-10">

                {/* Header */}
                <header className="mb-12 text-center">
                    <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-200 to-pink-200 mb-4 drop-shadow-lg">
                        Job Collector
                    </h1>
                    <p className="text-blue-200 text-lg opacity-80">
                        Curated Data & AI Roles • Auto-Scraped Daily
                    </p>
                </header>

                {/* Search Bar */}
                <div className="mb-12 max-w-2xl mx-auto">
                    <div className="glass-panel p-2 flex items-center">
                        <Search className="w-6 h-6 text-blue-300 ml-3" />
                        <input
                            type="text"
                            placeholder="Search by role or company..."
                            className="bg-transparent border-none outline-none text-white placeholder-blue-300/50 w-full p-3 text-lg"
                            value={filter}
                            onChange={(e) => setFilter(e.target.value)}
                        />
                    </div>
                </div>

                {/* Grid */}
                {loading ? (
                    <div className="text-center text-blue-300 animate-pulse">Loading jobs...</div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {filteredJobs.map((job) => (
                            <motion.div
                                key={job.id}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                whileHover={{ scale: 1.02 }}
                                className="glass-panel p-6 flex flex-col justify-between h-full hover:border-blue-400/50 transition-colors"
                            >
                                <div>
                                    <div className="flex justify-between items-start mb-4">
                                        <span className="bg-blue-500/20 text-blue-200 text-xs px-3 py-1 rounded-full border border-blue-500/30">
                                            {job.companies?.name || 'Unknown'}
                                        </span>
                                        <span className="text-xs text-gray-400 flex items-center gap-1">
                                            <Calendar className="w-3 h-3" /> {job.posted_date || 'Recent'}
                                        </span>
                                    </div>

                                    <h2 className="text-xl font-semibold mb-2 leading-tight text-white/90">
                                        {job.title}
                                    </h2>

                                    <div className="flex items-center gap-2 text-sm text-gray-300 mb-6">
                                        <MapPin className="w-4 h-4 text-pink-400" />
                                        {job.location}
                                    </div>
                                </div>

                                <a
                                    href={job.url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="glass-button w-full py-3 rounded-xl flex items-center justify-center gap-2 font-medium text-blue-100 group"
                                >
                                    Apply Now
                                    <ExternalLink className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                                </a>
                            </motion.div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    )
}

export default App
