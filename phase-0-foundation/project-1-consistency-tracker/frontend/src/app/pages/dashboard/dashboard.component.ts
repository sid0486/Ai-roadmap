import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { TaskService } from '../../core/services/task.service';
import { AuthService } from '../../core/services/auth.service';
import { Task } from '../../core/models/task.model';

interface DayDot {
  completed: boolean;
  today: boolean;
  future: boolean;
  todayPending: boolean;
}

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit {
  tasks: Task[] = [];
  newTaskTitle = '';
  loading = false;
  error = '';
  yearDays: DayDot[] = [];

  constructor(
    private taskService: TaskService,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  get todayIndex(): number {
    const today = new Date();
    const startOfYear = new Date(today.getFullYear(), 0, 1);
    return Math.floor(
      (today.getTime() - startOfYear.getTime()) / (1000 * 60 * 60 * 24)
    );
  }

  get currentDayOfYear(): number {
    return this.todayIndex + 1;
  }

  get currentYear(): number {
    return new Date().getFullYear();
  }

  get completedCount(): number {
    return this.tasks.filter(t => t.completed).length;
  }

  get bestStreak(): number {
    return this.tasks.reduce((max, t) => Math.max(max, t.streak || 0), 0);
  }

  getPastColor(index: number): string {
    const progress = index / Math.max(this.todayIndex, 1);
    const r = Math.round(160 - (progress * 60));
    const g = Math.round(140 - (progress * 80));
    const b = Math.round(255 - (progress * 40));
    return `rgba(${r}, ${g}, ${b}, ${0.3 + progress * 0.5})`;
  }

  generateYearGrid(): void {
    const idx = this.todayIndex;
    const hasCompletedToday = this.completedCount > 0;

    this.yearDays = Array.from({ length: 365 }, (_, i) => ({
      completed: i < idx,
      today: i === idx && hasCompletedToday,
      todayPending: i === idx && !hasCompletedToday,
      future: i > idx
    }));
  }

  loadTasks(): void {
    this.taskService.getTasks().subscribe({
      next: (tasks) => {
        this.tasks = tasks;
        this.generateYearGrid();
      },
      error: () => {
        this.error = 'Failed to load tasks. Please refresh the page.';
      }
    });
  }

  addTask(): void {
    if (!this.newTaskTitle.trim()) return;
    this.error = '';
    this.loading = true;

    this.taskService.createTask({ title: this.newTaskTitle }).subscribe({
      next: (task) => {
        this.tasks.push(task);
        this.newTaskTitle = '';
        this.loading = false;
        this.generateYearGrid();
      },
      error: (err) => {
        if (err.status === 400) {
          this.error = `Task "${this.newTaskTitle}" already exists!`;
        } else {
          this.error = err.error?.detail || 'Failed to create task. Please try again.';
        }
        this.loading = false;
      }
    });
  }

  toggleTask(task: Task): void {
    this.taskService.updateTask(task.id, {
      title: task.title,
      completed: !task.completed
    }).subscribe({
      next: (updated) => {
        const index = this.tasks.findIndex(t => t.id === updated.id);
        if (index !== -1) this.tasks[index] = updated;
        this.generateYearGrid();
      },
      error: () => {
        this.error = 'Failed to update task. Please try again.';
      }
    });
  }

  deleteTask(id: number): void {
    this.taskService.deleteTask(id).subscribe({
      next: () => {
        this.tasks = this.tasks.filter(t => t.id !== id);
        this.generateYearGrid();
      },
      error: () => {
        this.error = 'Failed to delete task. Please try again.';
      }
    });
  }

  logout(): void {
    this.authService.logout();
  }
}