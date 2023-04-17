use our_organization;

CREATE TABLE [dbo].[departments](
	[id] [int] NOT NULL,
	[department] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[pc](
	[pc_id] [varchar](36) NOT NULL,
	[pc_serial] [varchar](max) NULL,
	[pc_mac] [varchar](max) NULL,
	[pc_ip] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[pc_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[personal](
	[user_id] [varchar](36) NOT NULL,
	[first_name] [varchar](max) NULL,
	[last_name] [varchar](max) NULL,
	[birth_date] [date] NULL,
	[login] [varchar](max) NULL,
	[email] [varchar](max) NULL,
	[department_id] [int] NULL,
	[pc_id] [varchar](36) NULL,
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[personal]  WITH CHECK ADD FOREIGN KEY([department_id])
REFERENCES [dbo].[departments] ([id])
GO

ALTER TABLE [dbo].[personal]  WITH CHECK ADD FOREIGN KEY([pc_id])
REFERENCES [dbo].[pc] ([pc_id])
GO

CREATE TABLE [dbo].[contracts](
	[user_id] [varchar](36) NOT NULL,
	[date_from] [date] NULL,
	[date_to] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[contracts]  WITH CHECK ADD FOREIGN KEY([user_id])
REFERENCES [dbo].[personal] ([user_id])
GO

CREATE TABLE [dbo].[salary](
	[salary_id] [int] IDENTITY(1,1) NOT NULL,
	[user_id] [varchar](36) NULL,
	[month] [int] NULL,
	[year] [int] NULL,
	[salary] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[salary_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[user_id] ASC,
	[month] ASC,
	[year] ASC,
	[salary] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[salary]  WITH CHECK ADD FOREIGN KEY([user_id])
REFERENCES [dbo].[personal] ([user_id])
GO

CREATE TABLE [dbo].[login_dates](
	[login_dates_id] [int] IDENTITY(1,1) NOT NULL,
	[user_id] [varchar](36) NULL,
	[pc_id] [varchar](36) NULL,
	[date_time] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[login_dates_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[user_id] ASC,
	[pc_id] ASC,
	[date_time] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[login_dates]  WITH CHECK ADD FOREIGN KEY([pc_id])
REFERENCES [dbo].[pc] ([pc_id])
GO

ALTER TABLE [dbo].[login_dates]  WITH CHECK ADD FOREIGN KEY([user_id])
REFERENCES [dbo].[personal] ([user_id])
GO