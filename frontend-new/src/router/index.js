import { createRouter, createWebHistory } from 'vue-router'

import SearchBar from '@/components/SearchBar.vue'
import PlayerView from '@/views/PlayerView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/searchbar',
            name: 'SearchBar',
            component: SearchBar,
        },
        {
            path: '/player/:id',
            name: 'PlayerDetail',
            component: PlayerView,
            props: true
        }
    ]
})

export default router