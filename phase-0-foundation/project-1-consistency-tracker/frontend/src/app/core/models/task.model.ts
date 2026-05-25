export interface Task {
  id: number;
  title: string;
  completed: boolean;
  streak: number;
  last_completed: string | null;
  created_at: string;
  user_id: number;
}

export interface TaskCreate {
  title: string;
}

export interface TaskUpdate {
  title: string;
  completed: boolean;
}