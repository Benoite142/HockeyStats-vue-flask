import { createRouter, createWebHistory } from 'vue-router'

import SearchBar from '@/components/SearchBar.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/searchbar',
            name: 'SearchBar',
            component: SearchBar,
        }
    ]
})

export default router