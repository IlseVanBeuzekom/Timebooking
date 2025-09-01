export interface Timebooking {
    id?: number;
    project_naam: string;
    ticket_nummer: string;
    beschrijving: string;
    date: Date;
    start_tijd: Date;
    eind_tijd: Date;
    duratie: number;
}