<template>
    <div class="home">
        <h1>Timebooking app</h1>
        <div class="recipe-tile">
            <div class="input">
                Input
            </div>
            <div class="project">
                <span>Projectnaam: </span>
                <input 
                    type="text"
                    v-model="projectNaamInput"
                    class="projectNaam"> 

                <span>Ticket nummer: </span>
                <input 
                    type="text"
                    v-model="ticketNummerInput"
                    class="ticketNummer">
            </div>
            <div class="beschrijving-div">
                <textarea class="beschrijving" name="Beschrijving" id="beschrijvingInput" v-model="beschrijvingInput"></textarea>
            </div>
            <button @click="startActiviteit">Start</button>
            <p>{{ beschrijvingInput }}</p>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue'
import { useTimeBookingApi } from '@/composables/useTimebookingApi';

export default {
    name: 'Home',
    setup() {
        const beschrijvingInput = ref('');
        const projectNaamInput = ref('');
        const ticketNummerInput = ref('');

        const projectNaamStarted = ref('');
        const ticketNummerStarted = ref('');
        const beschrijvingStarted = ref('');

        const startTijd = ref(new Date());
        const durationInSeconds = ref(0);

        const { addTimebooking }= useTimeBookingApi();

        const startActiviteit = async () => {
            endPreviousActivity();
            startNewActivity();            
        }

        const endPreviousActivity = async () => {
            if (projectNaamStarted.value){
                const startTijdPrevious = startTijd.value;
                const endTijdPrevious = new Date();
                const durationInMilliSecondsPrevious = (endTijdPrevious - startTijdPrevious);

                const {hours, minutes, seconds} = convertDurationToHoursMinutesSeconds(durationInMilliSecondsPrevious);
                
                const activityEntry = { 
                                        project_naam: projectNaamStarted.value
                                      , ticket_nummer: ticketNummerStarted.value
                                      , beschrijving: beschrijvingStarted.value
                                      , date: startTijdPrevious.toISOString().split('T')[0]
                                      , start_tijd: startTijdPrevious
                                      , eind_tijd: endTijdPrevious
                                      , duratie: durationInMilliSecondsPrevious / 1000
                }
                console.log(activityEntry);

                // Make here the call to the backend to save the activityEntry
                await addTimebooking(activityEntry)
            }
            
        }

        const convertDurationToHoursMinutesSeconds = (durationInMilliSeconds ) => {
            const seconds = Math.floor((durationInMilliSeconds / 1000) % 60);
            const minutes = Math.floor((durationInMilliSeconds / (1000 * 60)) % 60);
            const hours = Math.floor((durationInMilliSeconds / (1000 * 60 * 60)) % 24);

            return { hours, minutes, seconds };
        }

        const startNewActivity = () => {
            projectNaamStarted.value = projectNaamInput.value;
            ticketNummerStarted.value = ticketNummerInput.value;
            beschrijvingStarted.value = beschrijvingInput.value;
            startTijd.value = new Date();
        }

        return { projectNaamInput
               , ticketNummerInput
               , projectNaamStarted
               , ticketNummerStarted
               , startTijd
               , durationInSeconds
               , beschrijvingInput
               , endPreviousActivity
               , startNewActivity
               , startActiviteit
               , convertDurationToHoursMinutesSeconds
            }
    }
}
</script>

<style scoped>
.home {
    max-width: 800px;
    margin: 0 auto;
    padding: 48px 24px;
    
}

.recipe-tile {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    padding: 1rem;
    min-width: 180px;
    max-width: 800px;
    display: flex;
    flex-direction: column;
    cursor: pointer;
    transition: box-shadow 0.2s transform 0.2s;
    outline: none;
    position: relative;
}

.input {
    font-size: 1.25rem;
    text-align: left;
    justify-self: left;
    justify-content: left;
    margin-bottom: 1rem;
}

.beschrijving {
    width: 100%;
    height: 100px;
    margin-top: 1rem;
    margin-bottom: 1rem;

}

.projectNaam {
    margin-right: 1rem;
    width: 200px;
}

.ticketNummer {
    width: 100px;
}
</style>