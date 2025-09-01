import type { Timebooking } from '@/types/timebooking';

import { ref } from 'vue';

export function useTimeBookingApi() {
    const loading = ref(false);
    const error = ref<string|null>(null);

    async function addTimebooking(timebooking: Omit<Timebooking, 'id'>) {
        loading.value = true;
        error.value = null;
        try {
            const response = await fetch('http://localhost:3000/timebookings/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(timebooking)
            })
            if (!response.ok) {
                throw new Error('Failed to add timebooking');
            }
            return await response.json();
        } catch (err: any) {
            error.value = err.message || "Unknown error";
            throw err;
        } finally {
            loading.value = false;
        }
    }

    async function getTimebookingsByDate(date: string) {
        loading.value = true;
        error.value = null;

        try{
            const response = await fetch(`http://localhost:3000/timebookings/${date}`);
            if (!response.ok) {
                throw new Error('Failed to get timebookings');
            }
            return await response.json();
        }
        catch (err: any ) {
            error.value = err.message || "Unknown error";
            throw err;
        }
    }

    return { addTimebooking, getTimebookingsByDate }
}